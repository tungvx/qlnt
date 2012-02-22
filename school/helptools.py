# -*- coding: utf-8 -*-


from school.school_settings import *
from sms.views import *
import os
from django.db import transaction
#from SOAPpy import WSDL
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from viewMark import CHECKED_DATE
from writeExcel import normalize
SYNC_RESULT = os.path.join('helptool','recover_marktime.html')
SYNC_SUBJECT = os.path.join('helptool','sync_subject.html')
TEST_TABLE = os.path.join('helptool','test_table.html')
REALTIME = os.path.join('helptool','realtime_test.html')
CONVERT_MARK= os.path.join('helptool','convert_mark.html')
def convert_data_1n_mn(request):
    classes = Class.objects.all()
    for _class in classes:
        print _class.attend_set.all()
    students = Pupil.objects.all()
    for student in students:
        _class = student.class_id
        if not _class:
            print student, student.get_school()
        else:
            student.join_class(_class, student.school_join_date)
    message = 'Done'
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )


def recover_marktime(request):
    
    marks = Mark.objects.all()
    number_of_defect = 0
    
    if request.method == 'POST':
        for mark in marks:
            try:
                temp = mark.marktime
            except Exception as e:
                a = MarkTime()
                a.mark_id = mark
                a.save()
                number_of_defect +=1
        message = u'Bạn vừa tạo ' + str(number_of_defect) + u' MarkTime records'
    else:
        for mark in marks:
            try:
                temp = mark.marktime
            except Exception as e:
                number_of_defect += 1
        message = u'Thiếu ' + str(number_of_defect) + u'MarkTime records'
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )

def make_setting(request):

    orgs = Organization.objects.all()
    for org in orgs:
        if org.level == u'T':
            school = org
            try:
                last_year = school.year_set.latest('time')
                lock_time = school.get_setting('lock_time')
                if int(lock_time) == 24:
                    school.save_settings('lock_time', 24)
                print org
                classes = last_year.class_set.all()
                class_labels = u'['
                for _class in classes:
                    names = _class.name.split(' ')
                    if len(names) > 1:
                        try:
                            a = int(names[0])
                            class_labels += "u'%s'," % ' '.join(names)
                        except Exception as e:
                            print e
                            continue
                class_labels = class_labels[:-1] + u']'
                school.save_settings('class_labels', class_labels)
            except Exception as e:
                continue
    message = 'done'
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )


@transaction.commit_on_success
def sync_index(request):

    classes = Class.objects.all()
    message = ''
    try:
        for _class in classes:
            students = _class.pupil_set.order_by('index')
            index = 0
            for student in students:
                index +=1
                print student.index, index
                if not student.first_name.strip():
                    message += '\n' + student.last_name + ': wrong name'
                    names = student.last_name.strip().split(' ')
                    last_name = ' '.join(names[:len(names)-1])
                    first_name = names[len(names)-1]
                    try:
                        student.first_name = first_name
                        student.last_name = last_name
                        student.save()
                    except Exception as e:
                        print e
                if student.index != index:
                    student.index = index
                    student.save()
            _class.max = index
            _class.save()

    except Exception as e:
        print e
    message += '\n' + u'Sync xong index.'
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )

@transaction.commit_on_success
def copy_hanh_kiem_data(request):

    try:
        students = Pupil.objects.all()
        number = 0
        message = ''
        for student in students:
            tbnams = TBNam.objects.filter(student_id = student)
            for tbnam in tbnams:
                print tbnam.student_id, tbnam.year_id
                hk = HanhKiem.objects.filter(student_id=student, year_id=tbnam.year_id )
                if len(hk)>1:
                    for h in hk:
                        print h.student_id, h.year_id, h.term1, h.term2, h.year, h.ren_luyen_lai, h.hk_ren_luyen_lai
                number += 1
                tbnam.term1 = hk[0].term1
                tbnam.term2 = hk[0].term2
                tbnam.year = hk[0].year
                tbnam.ren_luyen_lai = hk[0].ren_luyen_lai
                tbnam.hk_ren_luyen_lai = hk[0].hk_ren_luyen_lai
                tbnam.save()
    except Exception as e:
        print e
    message += '\n' + u'Copy xong.' + str(number)
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )

@transaction.commit_on_success
def sync_subject(request):
    classes = Class.objects.all()
    print classes
    message = ''
    number = 0
    try:
        if request.method == 'GET':
            print 'get'
            for _class in classes:
                if not _class.subject_set.count():
                    number+=1
            print 'message'
            message = u'<p>Have ' + str(number) + ' classes those have no subject.</p>'

            number = 0
            subjects = Subject.objects.all()
            for subject in subjects:
                if subject.primary:
                    number += 1
            message += u'<br><p>%s subjects in database have non zero primary </p>' % number
        elif  request.method == 'POST':
            print 'POST'
            if 'sync' in request.POST:
                for _class in classes:
                    school = _class.year_id.school_id
                    if not school.status:
                        school.status = 1
                        school.save()
                    if school.school_level == '1': ds_mon_hoc = CAP1_DS_MON
                    elif school.school_level == '2': ds_mon_hoc = CAP2_DS_MON
                    elif school.school_level == '3': ds_mon_hoc = CAP3_DS_MON
                    else: raise Exception('SchoolLevelInvalid')

                    if not _class.subject_set.count():
                        index = 0
                        for mon in ds_mon_hoc:
                            index +=1
                            print index
                            add_subject(subject_name= mon, subject_type= mon, _class=_class, index=index)
                message = '<p>Syncing subject from all classes: Done </p>'
                print 'tag'
                subjects = Subject.objects.all()
                for subject in subjects:
                    if subject.primary == 1:
                        subject.primary = 0
                        subject.save()
                message += "<br><p>Syncing subject's primary: Done</p>"
        context = RequestContext(request)
        return render_to_response(SYNC_SUBJECT, {'message': message, 'number': number},
                                  context_instance = context)
    except Exception as e:
        print e


@transaction.commit_on_success
def check_logic(request):
    message = ''
    number = 0
    try:
        if request.method == 'GET':
            print 'get'
#            students = Pupil.objects.all()
#            for student in students:
#                marks = Mark.objects.filter(student_id__exact = student)
#                for mark in marks:
#                    if student.class_id.year_id.school_id != mark.subject_id.class_id.year_id.school_id:
#                        number+=1
#                        print student, student.class_id, student.class_id.year_id.school_id, mark.subject_id.class_id, mark.subject_id.class_id.year_id.school_id, mark.subject_id
#            print 'message'
            tkmons = TKMon.objects.all()
            wrong_logic = 0
            for tk in tkmons:
                student = tk.student_id
                subject = tk.subject_id
                if student.class_id != subject.class_id:
                    wrong_logic += 1

            message = u'<p>Have ' + str(number) + ','+ str(wrong_logic) + ' students that have bugs.</p>'

            number = 0
            classes = Class.objects.all()
            for _class in classes:
                expected_tkmon_number = _class.subject_set.count() * _class.students().count()
                tkmon_number = 0
                subjects = Subject.objects.filter( class_id = _class)
                for subject in subjects:
                    tkmon_number += subject.tkmon_set.count()
                if expected_tkmon_number != tkmon_number:
                    message += r'<li>'+unicode(_class.year_id.school_id) + ':'\
                               + unicode(_class)+':' \
                               + str(expected_tkmon_number) + '----' + str(tkmon_number) + r'</li>'
                number += _class.subject_set.count() * _class.students().count()
            message += r'<li>' + 'Expected tkmon: ' + str(number) + r'</li>'
            message += ':' + str(TKMon.objects.count())
            tkmons = TKMon.objects.all()
            if number == TKMon.objects.count():
                message += 'OK'
        elif  request.method == 'POST':
            print 'POST'
            message = ''
            number = 0
            classes = Class.objects.all()
            for _class in classes:
                subjects = _class.subject_set.all()
                students = _class.pupil_set.all()
                for student in students:
                    for subject in subjects:
                        a = TKMon.objects.filter(student_id = student, subject_id = subject)
                        if not a:

                            print '*', student.get_school(), student.class_id, student, subject
                            a = TKMon.objects.create(student_id = student, subject_id = subject)
                            number += 1
                        elif len(a) >= 2:
                            print '__',student.get_school(), student.class_id, student, subject
                            aa = a[1]
                            aa.delete()
            message += r'Done:' + str(number)
#            if 'sync' in request.POST:
#                for _class in classes:
#                    school = _class.year_id.school_id
#                    if not school.status:
#                        school.status = 1
#                        school.save()
#                    if school.school_level == '1': ds_mon_hoc = CAP1_DS_MON
#                    elif school.school_level == '2': ds_mon_hoc = CAP2_DS_MON
#                    elif school.school_level == '3': ds_mon_hoc = CAP3_DS_MON
#                    else: raise Exception('SchoolLevelInvalid')
#
#                    if not _class.subject_set.count():
#                        index = 0
#                        for mon in ds_mon_hoc:
#                            index +=1
#                            print index
#                            add_subject(subject_name= mon, subject_type= mon, _class=_class, index=index)
#                message = '<p>Syncing subject from all classes: Done </p>'
#                print 'tag'
#                subjects = Subject.objects.all()
#                for subject in subjects:
#                    if subject.primary == 1:
#                        subject.primary = 0
#                        subject.save()
#                message += "<br><p>Syncing subject's primary: Done</p>"
        context = RequestContext(request)
        return render_to_response(SYNC_SUBJECT, {'message': message, 'number': number},
                                  context_instance = context)
    except Exception as e:
        print e


@transaction.commit_on_success
def sync_subject_type(request):
    message = ''
    number = 0
    try:
        if request.method == 'GET':
            print 'get'
            number = 0
            subjects = Subject.objects.all()
            for subject in subjects:
                if (not subject.type) or subject.name == u'Giáo dục công dân':
                    number += 1
            message += u'<br><p>%s subjects in database do not have correct type </p>' % number
        elif  request.method == 'POST':
            print 'POST'
            if 'sync' in request.POST:
                print 'tag'
                subjects = Subject.objects.all()
                for subject in subjects:
                    if (not subject.type) or subject.name == u'Giáo dục công dân':
                        if subject.name.lower() == u'Giáo dục quốc phòng'.lower():
                            subject.type = u'GDQP-AN'
                        elif subject.name.lower() == u'Giáo dục công dân'.lower():
                            subject.type = u'GDCD'
                        else:
                            subject.type = subject.name
                        subject.save()
                message += "<br><p>Syncing subject's type: Done</p>"
        context = RequestContext(request)
        return render_to_response(SYNC_SUBJECT, {'message': message, 'number': number},
                                  context_instance = context)
    except Exception as e:
        print e

@transaction.commit_on_success
def sync_subject_primary(request):
    subjects = Subject.objects.all()
    for subject in subjects:
        if subject.primary:
            subject.primary = 0
            subject.save()
    message = "Syncing subject's primary is done"
    context = RequestContext(request)
    return render_to_response( SYNC_RESULT, { 'message' : message},
                               context_instance = context )


def test_table(request):
    context = RequestContext(request)
    school = get_school(request)
    student_list = [x for x in range(1,70)]
    mark_list = [x for x in range(1,20)]
    return render_to_response( TEST_TABLE, {'mark_list': mark_list,
                                            'student_list': student_list}, context_instance = context)

def realtime(request):
    print request.session.session_key
    return render_to_response( REALTIME, {
        "user":request.user,
        "CHANNEL_NAME":'message',
        "STOMP_PORT":settings.STOMP_PORT,
        "HOST":settings.INTERFACE,
        "SESSION_COOKIE_NAME": settings.SESSION_COOKIE_NAME
    }, context_instance = RequestContext(request))

#class myHTTPTransport(HTTPTransport):
#    username = None
#    password = None
#    @classmethod
#    def setAuthen(cls, u, p):
#        cls.username = u
#        cls.password = p
#    def call(self, addr, data, namespace, soapaction=None,
#             encoding=None, http_proxy=None, config=Config, timeout=None):
#        if not isinstance(addr, SOAPAddress):
#            addr=SOAPAddress(addr, config)
#        if self.username != None:
#            addr.user = self.username + ':' + self.password
#        return HTTPTransport.call(self, addr, data, namespace, soapaction, encoding, http_proxy, config, timeout)
def convertaMark(mark,sent,time,markStr,markSMS,markTime,pre,number):
    if mark!=None:
        markStr+='*'*(number-pre)+normalize(mark)
        if time==None:
            markTime+='*'*(number-pre)
        else:
            markTime+='*'*(number-pre)+str(int((time-CHECKED_DATE).total_seconds()/60))
        if sent=='1':
            markSMS+='*'*(number-pre)+'1'
        else:
            markSMS+='*'*(number-pre)
        pre=number
        
    return markStr,markSMS,markTime,pre

@transaction.commit_on_success
def convertMark(request):

    #subjects = Subject.objects.filter(id=328)
    subjects = Subject.objects.all()
    tong=0
    for s in subjects:
        #print "fffffffffffffff",to_en1(s.class_id.year_id.school_id.name)
        tong+=1
        if tong % 10==0: print tong
        #print tong
        for i in range(1,3):
            markList =Mark.objects.filter(subject_id=s.id,term_id__number=i).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
            timeList =MarkTime.objects.filter(mark_id__subject_id=s.id,mark_id__term_id__number=i).order_by('mark_id__student_id__index','mark_id__student_id__first_name','mark_id__student_id__last_name','mark_id__student_id__birthday')
            tkMonList=TKMon.objects.filter(subject_id=s.id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
            for m,mt,tkMon in zip(markList,timeList,tkMonList):

                miengStr=''
                miengSMS=''
                miengTime=''
                pre=1
                miengStr,miengSMS,miengTime,pre=convertaMark(m.mieng_1,m.sent_mark[0],mt.mieng_1,miengStr,miengSMS,miengTime,pre,1)
                miengStr,miengSMS,miengTime,pre=convertaMark(m.mieng_2,m.sent_mark[1],mt.mieng_2,miengStr,miengSMS,miengTime,pre,2)
                miengStr,miengSMS,miengTime,pre=convertaMark(m.mieng_3,m.sent_mark[2],mt.mieng_3,miengStr,miengSMS,miengTime,pre,3)
                miengStr,miengSMS,miengTime,pre=convertaMark(m.mieng_4,m.sent_mark[3],mt.mieng_4,miengStr,miengSMS,miengTime,pre,4)
                miengStr,miengSMS,miengTime,pre=convertaMark(m.mieng_5,m.sent_mark[4],mt.mieng_5,miengStr,miengSMS,miengTime,pre,5)

                mlamStr=''
                mlamSMS=''
                mlamTime=''
                pre=1
                mlamStr,mlamSMS,mlamTime,pre=convertaMark(m.mlam_1,m.sent_mark[5],mt.mlam_1,mlamStr,mlamSMS,mlamTime,pre,1)
                mlamStr,mlamSMS,mlamTime,pre=convertaMark(m.mlam_2,m.sent_mark[6],mt.mlam_2,mlamStr,mlamSMS,mlamTime,pre,2)
                mlamStr,mlamSMS,mlamTime,pre=convertaMark(m.mlam_3,m.sent_mark[7],mt.mlam_3,mlamStr,mlamSMS,mlamTime,pre,3)
                mlamStr,mlamSMS,mlamTime,pre=convertaMark(m.mlam_4,m.sent_mark[8],mt.mlam_4,mlamStr,mlamSMS,mlamTime,pre,4)
                mlamStr,mlamSMS,mlamTime,pre=convertaMark(m.mlam_5,m.sent_mark[9],mt.mlam_5,mlamStr,mlamSMS,mlamTime,pre,5)

                motTietStr=''
                motTietSMS=''
                motTietTime=''
                pre=1
                motTietStr,motTietSMS,motTietTime,pre=convertaMark(m.mot_tiet_1,m.sent_mark[10],mt.mot_tiet_1,motTietStr,motTietSMS,motTietTime,pre,1)
                motTietStr,motTietSMS,motTietTime,pre=convertaMark(m.mot_tiet_2,m.sent_mark[11],mt.mot_tiet_2,motTietStr,motTietSMS,motTietTime,pre,2)
                motTietStr,motTietSMS,motTietTime,pre=convertaMark(m.mot_tiet_3,m.sent_mark[12],mt.mot_tiet_3,motTietStr,motTietSMS,motTietTime,pre,3)
                motTietStr,motTietSMS,motTietTime,pre=convertaMark(m.mot_tiet_4,m.sent_mark[13],mt.mot_tiet_4,motTietStr,motTietSMS,motTietTime,pre,4)
                motTietStr,motTietSMS,motTietTime,pre=convertaMark(m.mot_tiet_5,m.sent_mark[14],mt.mot_tiet_5,motTietStr,motTietSMS,motTietTime,pre,5)

                diem=miengStr +'|'+mlamStr+'|'+motTietStr
                sent=miengSMS +'|'+mlamSMS+'|'+motTietSMS
                time=miengTime+'|'+mlamTime+'|'+motTietTime
                #####################################################
                if m.ck!=None:
                    #diem+='|'+normalize(m.ck)
                    if (mt.ck==None):
                        time+='|'
                    else:
                        time+='|'+str(int((mt.ck-CHECKED_DATE).total_seconds()/60))
                    if m.sent_mark[15]==1:
                        sent+='|1'
                    else:
                        sent+='|'
                else:
                    #diem+='|'
                    sent+='|'
                    time+='|'
                #########################
                if m.tb!=None:
                    #diem+='|'+normalize(m.tb)
                    if (mt.tb==None):
                        time+='|'
                    else:
                        time+='|'+str(int((mt.tb-CHECKED_DATE).total_seconds()/60))
                    if i==1:
                        if m.sent_mark[16]==1:
                            sent+='|1'
                        else:
                            sent+='|'
                    else:
                        if m.sent_mark[17]==1:
                            sent+='|1'
                        else:
                            sent+='|'
                else:
                    #diem+='|'
                    sent+='|'
                    time+='|'

                if i==2:
                    if m.sent_mark[18]=='1':
                        tkMon.sent=True
                    else:
                        tkMon.sent=False

                m.diem=diem
                m.sent=sent
                m.time=time
                m.save()
                tkMon.save()

#
#                print m.mieng_1,m.mieng_2,m.mieng_3,m.mieng_4,m.mieng_5,
#                print m.mlam_1,m.mlam_2,m.mlam_3,m.mlam_4,m.mlam_5,
#                print m.mot_tiet_1,m.mot_tiet_2,m.mot_tiet_3,m.mot_tiet_4,m.mot_tiet_5
#                print m.ck,' ',m.tb
#                print diem
#                print sent
#                print time
#                print
#
    print CHECKED_DATE
    message = "convert is done"
    context = RequestContext(request)
    return render_to_response( CONVERT_MARK, { 'message' : message},
                               context_instance = context )