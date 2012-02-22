﻿# author: luulethe@gmail.com 

# -*- coding: utf-8 -*-
#from school.views import *

from django.http import HttpResponse, HttpResponseRedirect
from school.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from school.viewCount import *
from school.utils import *
from django.core.urlresolvers import reverse
from django.db import transaction
from django.utils import simplejson
import time
import os.path 
from school.sms_views import sendSMS

ENABLE_CHANGE_MARK=True
e=0.00000001
def finish(request):
    
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    
    if (get_position(request) != 4):
        return HttpResponseRedirect('/school')
    
    message=None
    
    currentTerm=get_current_term(request)
    
    yearString = str(currentTerm.number)+"-"+str(currentTerm.number+1)
    firstTerm  =Term.objects.get(year_id=currentTerm.year_id,number=1)
    secondTerm  =Term.objects.get(year_id=currentTerm.year_id,number=2)
    
    
    t = loader.get_template(os.path.join('school/finish','finish.html'))
    c = RequestContext(request, {"message":message,
                                 'yearString':yearString,
                                 'firstTerm':firstTerm,
                                 'secondTerm':secondTerm,
                                 'currentTerm':currentTerm,
                                }
                       )
    return HttpResponse(t.render(c))

# tinh diem tong ket cho 1 lop theo hoc ky
def defineHl(tb,monChuyen,monToan,monVan,minMark):
    if monChuyen:
        firstMark=monChuyen.tb+e
    elif monToan.tb<monVan.tb:
        firstMark=monVan.tb+e
    else:
        firstMark=monToan.tb+e                
    
    if (tb>=8.0) & (firstMark>=8.0) & (minMark>=6.5):
        return 'G'
    elif (tb>=8.0) & (minMark>=5):
        return 'K'
    elif (tb>=8.0):
        return 'TB'
    elif (tb>=6.5) & (firstMark>=6.5) & (minMark>=5):
        return 'K'
    elif (tb>=6.5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=6.5): 
        return 'Y'
    elif (tb>=5) & (firstMark>=5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=3.5) & (minMark>=2):
        return 'Y'
    else:
        return 'Kem'

def defineHlThiLai(tb,monChuyen,monToan,monVan,minMark):
    
    if monToan.diem_thi_lai!=None:
        diemToan=monToan.diem_thi_lai
    else:
        diemToan=monToan.tb_nam
        
    if monVan.diem_thi_lai!=None:
        diemVan=monVan.diem_thi_lai
    else:
        diemVan=monVan.tb_nam
    
    if monChuyen:
        if monChuyen.diem_thi_lai!=None:
            firstMark=monChuyen.diem_thi_lai+e
        else:    
            firstMark=monChuyen.tb_nam+e
    elif diemToan<diemVan:
        firstMark=diemVan+e
    else:
        firstMark=diemToan+e                
    
    if (tb>=8.0) & (firstMark>=8.0) & (minMark>=6.5):
        return 'G'
    elif (tb>=8.0) & (minMark>=5):
        return 'K'
    elif (tb>=8.0):
        return 'TB'
    elif (tb>=6.5) & (firstMark>=6.5) & (minMark>=5):
        return 'K'
    elif (tb>=6.5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=6.5): 
        return 'Y'
    elif (tb>=5) & (firstMark>=5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=3.5) & (minMark>=2):
        return 'Y'
    else:
        return 'Kem'


def defineHlNam(tb,monChuyen,monToan,monVan,minMark):
    if monChuyen:
        firstMark=monChuyen.tb_nam+e
    elif monToan.tb_nam>monVan.tb_nam:
        firstMark=monToan.tb_nam+e
    else:
        firstMark=monVan.tb_nam+e                
    
    if (tb>=8.0) & (firstMark>=8.0) & (minMark>=6.5):
        return 'G'
    elif (tb>=8.0) & (minMark>=5):
        return 'K'
    elif (tb>=8.0):
        return 'TB'
    elif (tb>=6.5) & (firstMark>=6.5) & (minMark>=5):
        return 'K'
    elif (tb>=6.5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=6.5): 
        return 'Y'
    elif (tb>=5) & (firstMark>=5) & (minMark>=3.5):
        return 'TB'
    elif (tb>=3.5) & (minMark>=2):
        return 'Y'
    else:
        return 'Kem'
    
    
#tinh diem tong ket cua mot lop theo hoc ky
#def overallForAStudentInTerm(markList,tbHocKy,vtMonChuyen,vtMonToan,vtMonVan):
@transaction.commit_on_success
def calculateOverallMarkTerm(class_id,termNumber):
    
    selectedClass=Class.objects.get(id=class_id)
    selectedTerm =Term.objects.get(year_id=selectedClass.year_id,number=termNumber)     
    ddhkList    =TKDiemDanh.objects.filter(student_id__classes=class_id,term_id=selectedTerm).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    for ddhk in ddhkList:        
        ddhk.co_phep=DiemDanh.objects.filter(student_id=ddhk.student_id,term_id=selectedTerm,loai=u'Có phép').count()
        ddhk.khong_phep=DiemDanh.objects.filter(student_id=ddhk.student_id,term_id=selectedTerm,loai=u'Không phép').count()
        ddhk.tong_so=ddhk.co_phep+ddhk.khong_phep
        ddhk.save()
        
    pupilNoSum =0
    subjectList=Subject.objects.filter(class_id=class_id,primary__in=[0,termNumber]).order_by('index','name')    
    markList = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=termNumber,current=True,subject_id__primary__in=[0,termNumber]).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
    tbHocKyList = TBHocKy.objects.filter(student_id__classes=class_id,term_id__number=termNumber).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    hkList      = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    length=len(subjectList)
    i=0   
    vtMonChuyen=-1
    checkComment=[0]*len(subjectList)
    for s in subjectList:
        if s.hs==3:  vtMonChuyen=i
                    
        if    s.name.lower().__contains__(u'toán'):
            vtMonToan=i
        elif  s.name.lower().__contains__(u'văn'):
            vtMonVan=i
        if s.nx:
            checkComment[i]=1        
        i+=1    
    i=0
    j=0
    # cam xoa dong nay
    for tt in tbHocKyList:
        pass
    
    for m in markList:
        #print i
        t= i % length
        if t==0:
            ok=True
            monChuyen=None
            monToan  =None
            monVan   =None
            minMark  =10
            markSum=0
            factorSum=0
            tbHocKy=tbHocKyList[j]
            j+=1                       
             
        if t==vtMonChuyen  :  monChuyen=m
             
        if   t==vtMonToan  :
            monToan=m
        elif t==vtMonVan   :  
            monVan =m
        if (m.tb !=None):
            if m.mg==False:
                if checkComment[t]==0:
                    markSum += m.tb*subjectList[t].hs
                    factorSum +=subjectList[t].hs 
                  
                if m.tb<minMark:
                    minMark=m.tb
        else:
            if m.mg==False:
                ok=False    
        if (t==length-1):
             
            if  ok:
                if factorSum==0:     
                    tbHocKy.tb_hk=None
                    tbHocKy.hl_hk=None
                else:
                    tbHocKy.tb_hk=round(markSum/factorSum+e,1)                                
                    tbHocKy.hl_hk=defineHl(tbHocKy.tb_hk+e,monChuyen,monToan,monVan,minMark+e)
            else:
                tbHocKy.tb_hk=None
                tbHocKy.hl_hk=None
                pupilNoSum+=1
                
            #tbHocKy.save()                    
        i+=1        
    NN2List = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=termNumber,subject_id__primary=3,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    if len(NN2List)>0:
        for nn2,tbHocKy in zip(NN2List,tbHocKyList):
            if    nn2.tb+e>=8  : tbHocKy.tb_hk+=0.3
            elif  nn2.tb+e>=6.5: tbHocKy.tb_hk+=0.2
            elif  nn2.tb+e>=5  : tbHocKy.tb_hk+=0.1
    
    for hk in hkList :
        pass
    
    noHanhKiem = 0
    for hk,tbHocKy in zip(hkList,tbHocKyList):
        if termNumber==1: loaiHk=hk.term1
        else            : loaiHk=hk.term2
        
        if loaiHk==None: noHanhKiem+=1
        if (loaiHk==None) | (tbHocKy.hl_hk==None):
            tbHocKy.danh_hieu_hk=None
        elif (loaiHk=='T') & (tbHocKy.hl_hk=='G'): 
            tbHocKy.danh_hieu_hk='G'
        elif ((loaiHk=='T') | (loaiHk=='K')) & ((tbHocKy.hl_hk=='G') | (tbHocKy.hl_hk=='K')):
            tbHocKy.danh_hieu_hk='TT'
        else: tbHocKy.danh_hieu_hk='K'                                         
    
    
    
              
    for tb in tbHocKyList:
        tb.save()                       
       
    return pupilNoSum,noHanhKiem
@transaction.commit_on_success
def calculateTKMon(class_id):
    
    cnList = TKMon.objects.filter(subject_id__class_id=class_id,subject_id__primary=1,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
    hk1List = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=1,subject_id__primary=1,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 

    #print cnList
    for hk1,cn in zip(hk1List,cnList):
        cn.tb_nam = hk1.tb

    cn1List = TKMon.objects.filter(subject_id__class_id=class_id,subject_id__primary=2,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
    hk2List = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=2,subject_id__primary=2,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 

    #print cn1List
    for hk2,cn in zip(hk2List,cn1List):
        cn.tb_nam = hk2.tb
        
    for cn in cnList:
        cn.save()

    for cn in cn1List:
        cn.save()

          
@transaction.commit_on_success
def calculateOverallMarkYear(class_id=7):

    pupilNoSum =0
    subjectList= Subject.objects.filter(class_id=class_id,primary__in=[0,1,2]).order_by("index",'name')    
    markList   = TKMon.objects.filter(subject_id__class_id=class_id,subject_id__primary__in=[0,1,2],current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
    tbNamList  = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    #calculateTKMon(class_id)

    length = len(subjectList)
    print length
    i=0   
    vtMonChuyen=-1
    for s in subjectList:
        if s.hs==3:  vtMonChuyen=i
                    
        if    s.name.lower().__contains__(u'toán'):
            vtMonToan=i
        elif  s.name.lower().__contains__(u'văn'):
            vtMonVan=i    
        i+=1    
    i=0
    j=0  
    # cam xoa dong nay
    for t in tbNamList:
        pass
    for m in markList:
        t= i % length
        if t==0:
            ok=True
            monChuyen=None
            monToan  =None
            monVan   =None
            minMark  =10
            markSum=0
            factorSum=0   
            tbNam=tbNamList[j]
            j+=1                       
             
        if t==vtMonChuyen  :  monChuyen=m
             
        if   t==vtMonToan  :
            monToan=m
        elif t==vtMonVan   :  
            monVan =m
             
        if m.tb_nam !=None:
            if m.mg==False: 
                if subjectList[t].nx==False:   
                    markSum += m.tb_nam*subjectList[t].hs
                    factorSum +=subjectList[t].hs 
                  
                if m.tb_nam<minMark:
                    minMark=m.tb_nam
        else:
            if m.mg==False:            
                ok=False
        if (t==length-1):
            if  ok:
                if factorSum==0:     
                    tbNam.tb_nam=None
                    tbNam.hl_nam=None
                else:
                    
                    tbNam.tb_nam=round(markSum/factorSum+e,1)
                    tbNam.hl_nam=defineHlNam(tbNam.tb_nam+e,monChuyen,monToan,monVan,minMark+e)
            else:
                tbNam.tb_nam=None
                tbNam.hl_nam=None
                pupilNoSum+=1
        i+=1
    NN2List= TKMon.objects.filter(subject_id__class_id=class_id,subject_id__primary=3,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 

    if len(NN2List)>0:
        for nn2,tbNam in zip(NN2List,tbNamList):
            if (nn2.tb_nam!=None) & (tbNam.tb_nam!=None): 
                if  nn2.tb_nam+e>=8    : tbNam.tb_nam+=0.3
                elif  nn2.tb_nam+e>=6.5: tbNam.tb_nam+=0.2
                elif  nn2.tb_nam+e>=5  : tbNam.tb_nam+=0.1
        
    noHanhKiem = 0            
    for tbNam in tbNamList:
        loaiHk=tbNam.year
        
        if loaiHk==None: noHanhKiem+=1
        
        if (loaiHk==None) | (tbNam.hl_nam==None):
            tbNam.danh_hieu_nam=None
        elif (loaiHk=='T') & (tbNam.hl_nam=='G'): 
            tbNam.danh_hieu_nam='G'
        elif ((loaiHk=='T') | (loaiHk=='K')) & ((tbNam.hl_nam=='G') | (tbNam.hl_nam=='K')):
            tbNam.danh_hieu_nam='TT'
        else: tbNam.danh_hieu_nam='K'                                         
                
    for tb in tbNamList:
        tb.save()                       
       
    return pupilNoSum,noHanhKiem    
# xep loai hoc ky cua mot lop

def xepLoaiHlTheoLop(request,class_id,termNumber):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedClass = Class.objects.get(id__exact = class_id)
    
    try:
        if in_school(request,selectedClass.year_id.school_id) == False:
            return HttpResponseRedirect('/school')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))
    
    ok=False
    position = get_position(request)
    if position ==4: ok=True
    #kiem tra xem giao vien nay co phai chu nhiem lop nay khong
    if position ==3:
        if selectedClass.teacher_id != None:
            if selectedClass.teacher_id.user_id.id == request.user.id:
                ok=True
                 
    if (not ok):
        return HttpResponseRedirect('/school')


    message=None
    selectedYear  =selectedClass.year_id
    pupilList     =Pupil.objects.filter(classes=class_id,attend__is_member=True).order_by('index','first_name','last_name','birthday')    

    
    yearString = str(selectedYear.time)+"-"+str(selectedYear.time+1)
    tempList=[]
    list=[]
    # neu la hk1 hoac hk2
    termNumber=int(termNumber)
    
    if request.method=="POST":
        if termNumber <3 : noHl,noHk=calculateOverallMarkTerm(class_id,termNumber)
        else         : noHl,noHk=calculateOverallMarkYear(class_id)
        
        if (noHl==0) & (noHk==0):
            message="Đã có đủ điểm và hạnh kiểm của cả lớp"
        elif (noHl==0):
            message="Còn "+str(noHk)+" học sinh chưa có hạnh kiểm"
        elif (noHk==0):    
            message="Còn "+str(noHl)+" học sinh chưa đủ điểm "
        else:
            message="Còn "+str(noHl)+" học sinh chưa đủ điểm và "+str(noHk)+" học sinh chưa có hạnh kiểm"
                   
          
        
    if termNumber<3:        

        subjectList=Subject.objects.filter(class_id=class_id,primary__in=[0,termNumber,3,4]).order_by("index",'name')    
        markList = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=termNumber,subject_id__primary__in=[0,termNumber,3,4],current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
        tbHocKyList = TBHocKy.objects.filter(student_id__classes=class_id,term_id__number=termNumber).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        hkList      = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        hkList1 =[]
        if termNumber==1:
            for hk in hkList:
                hkList1.append(hk.term1)
        else:
            for hk in hkList:
                hkList1.append(hk.term2)
                                        
        length = len(subjectList)

        i=0    
        for m in markList:
            t= i % length
            if t ==0:
                markOfAPupil=[]
            if m.mg:
                  markOfAPupil.append("MG")
            elif m.tb==None:    
                  markOfAPupil.append("")
            elif subjectList[t].nx:
                markOfAPupil.append(convertMarkToCharacter1(m.tb))
            else:            
                markOfAPupil.append(m.tb)        
            
            if t==0:            
                tempList.append(markOfAPupil) 
            i+=1
 
        list=zip(pupilList,tempList,tbHocKyList,hkList1)    
    else:
        calculateTKMon(class_id)
        idYear = selectedYear.id
        subjectList=Subject.objects.filter(class_id=class_id).order_by("index",'name')    
        markList   =TKMon.objects.filter(subject_id__class_id=class_id,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
        tbNamList = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        length = len(subjectList)

        i=0    
        for m in markList:
            t= i % length
            if t ==0:
                markOfAPupil=[]
                
            if m.mg:
                  markOfAPupil.append("MG")
            elif m.tb_nam==None:    
                  markOfAPupil.append("")
            elif subjectList[t].nx:
                markOfAPupil.append(convertMarkToCharacter1(m.tb_nam))
            else:                  
                markOfAPupil.append(m.tb_nam)        
            
            if t==0:            
                tempList.append(markOfAPupil) 
            i+=1
 
        list=zip(pupilList,tempList,tbNamList,tbNamList)    
        
    

    t = loader.get_template(os.path.join('school/finish','xep_loai_hl_theo_lop.html'))

    t2=time.time()
    print (t2-t1)
    c = RequestContext(request, {"message":message, 
                                 "subjectList":subjectList,
                                 "list":list,
                                 "selectedClass":selectedClass,
                                 "termNumber":termNumber,
                                 "yearString":yearString,
                                 #"classList" :classList,
                                }
                       )
    

    return HttpResponse(t.render(c))

@transaction.commit_on_success                                                              
def xepLoaiLop(class_id):
    
    
    tbNamList    =TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    ddhk1List    =TKDiemDanh.objects.filter(student_id__classes=class_id,term_id__number=1).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    ddhk2List    =TKDiemDanh.objects.filter(student_id__classes=class_id,term_id__number=2).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    #repr(tbNamList)
    noHk=0
    noHl=0
    i=0
    for tbNam,ddhk1,ddhk2 in zip(tbNamList,ddhk1List,ddhk2List):
        i+=1
        
        #ddhk1.tong_so=DiemDanh.objects.filter(student_id=tbNam.student_id,term_id__number=1).count()
        #ddhk2.tong_so=DiemDanh.objects.filter(student_id=tbNam.student_id,term_id__number=2).count()
        if tbNam.year==None     : noHk+=1
        if tbNam.hl_nam==None: noHl+=1
        
        if (ddhk1.tong_so!=None) & (ddhk2.tong_so!=None):          
            tbNam.tong_so_ngay_nghi=ddhk1.tong_so+ddhk2.tong_so
        if tbNam.tong_so_ngay_nghi==None:
            continue                
        if (tbNam.hl_nam==None) |(tbNam.year==None):
            tbNam.danh_hieu_nam=None  
                
            if tbNam.tong_so_ngay_nghi>45:
                tbNam.len_lop=False
                tbNam.thi_lai=None
                tbNam.ren_luyen_lai=None
                
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
            else:    
                tbNam.len_lop=None
                tbNam.thi_lai=None
                tbNam.ren_luyen_lai=None
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                
        else:
            if (tbNam.hl_nam=='G') & (tbNam.year=='T'):
                tbNam.danh_hieu_nam='G'
            elif ((tbNam.hl_nam=='G') | (tbNam.hl_nam=='K') ) & ((tbNam.year=='T') | (tbNam.year=='K')):
                tbNam.danh_hieu_nam='TT'
            else:
                tbNam.danh_hieu_nam='K'
                
            
            if tbNam.tong_so_ngay_nghi>45:
                tbNam.len_lop=False
                tbNam.ren_luyen_lai=None
                tbNam.thi_lai=None
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                continue        

            if (tbNam.hl_nam!='Y') & (tbNam.hl_nam!='Kem') & (tbNam.year!='Y'):
                tbNam.len_lop=True
                tbNam.thi_lai=None
                tbNam.ren_luyen_lai=None
                
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                continue
    
            if ((tbNam.year!='Y') & (tbNam.hl_nam=='Y')):
                tbNam.len_lop=None
                tbNam.thi_lai=True
                tbNam.ren_luyen_lai=None
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                
            elif  ((tbNam.year=='Y')  & (tbNam.hl_nam!='Y') & (tbNam.hl_nam!='Kem')):
                tbNam.thi_lai=None
                tbNam.len_lop=None
                tbNam.ren_luyen_lai=True
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                
            else:
                tbNam.len_lop=False
                tbNam.thi_lai=None
                tbNam.ren_luyen_lai=None
                tbNam.hk_ren_luyen_lai=None
                tbNam.tb_thi_lai=None
                tbNam.hl_thi_lai=None
                
    for tb in tbNamList:
        tb.save()
    for dd in ddhk1List:
        dd.save()
    for dd in ddhk2List:
        dd.save()
    return noHl,noHk    
@transaction.commit_on_success                                                                                  
def xlCaNamTheoLop(request,class_id,type):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedClass = Class.objects.get(id__exact = class_id)
    try:
        if in_school(request,selectedClass.year_id.school_id) == False:
            return HttpResponseRedirect('/school')

    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

    ok=False
    position = get_position(request)
    if position ==4: ok=True
    #kiem tra xem giao vien nay co phai chu nhiem lop nay khong
    if position ==3:
        if selectedClass.teacher_id != None:
            if selectedClass.teacher_id.user_id.id == request.user.id:
                ok=True
                 
    if (not ok):
        return HttpResponseRedirect('/school')

    message=None
    if request.method=="POST":
        noHl,noHk=xepLoaiLop(class_id)
        if (noHl==0) & (noHk==0):
            message="Đã xếp loại xong cả lớp"
        elif (noHl==0):
            message="Còn "+str(noHk)+" học sinh chưa có hạnh kiểm"
        elif (noHk==0):    
            message="Còn "+str(noHl)+" học sinh chưa có học lực "
        else:
            message="Còn "+str(noHl)+" học sinh chưa có học lực và "+str(noHk)+" học sinh chưa có hạnh kiểm"
    

    pupilNoSum=0
    
    pupilList    =Pupil.objects.filter(classes=class_id,attend__is_member=True).order_by('index','first_name','last_name','birthday')
    tbNamList    =TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    
    pupilList1=[]
    tbNamList1=[]
    type=int(type)
    
    for p,tbNam in zip(pupilList,tbNamList):
        ok=False
        if   type==1: ok=True
        elif type==2:
            if (tbNam.len_lop==None) & (tbNam.thi_lai==None) & (tbNam.ren_luyen_lai==None): ok=True
        elif type==3:
            if tbNam.danh_hieu_nam=='G': ok=True
        elif type==4:
            if tbNam.danh_hieu_nam=='TT': ok=True
        elif type==5:
            if tbNam.len_lop==True: ok=True
        elif type==6:
            if tbNam.len_lop==False: ok=True
        elif type==7:
            if tbNam.thi_lai==True: ok=True            
        elif type==8:
            if tbNam.ren_luyen_lai==True: ok=True
        if ok:    
            pupilList1.append(p)
            tbNamList1.append(tbNam)
            #hanhKiemList1.append(hk)
            
    list= zip(pupilList1,tbNamList1)             
    #print list
    yearString=str(selectedClass.year_id.time)+"-"+str(selectedClass.year_id.time+1)
    t = loader.get_template(os.path.join('school/finish','xl_ca_nam_theo_lop.html'))
    t2=time.time()
    print (t2-t1)
    
    c = RequestContext(request, {"message":message,
                                 "selectedClass":selectedClass,
                                 "yearString":yearString,
                                 "list":list 
                                }
                       )
    

    return HttpResponse(t.render(c))

#------------------------------------------------------------------------------

# tong ket hoc ky, tinh lai toan bo hoc luc cua hoc sinh trong toan truong
# xem xet lop nao da tinh xong, lop nao chua xong de hieu truong co the chi dao
# co chuc nang ket thuc hoc ky
#-----------------------------------------------------------------------------



# liet ke danh sach cac lop da tinh xong hoc luc va cac  lop chua xong
def finishTermInSchool(term_id):
    selectedTerm = Term.objects.get(id=term_id)
    classList=Class.objects.filter(year_id=selectedTerm.year_id)
    termNumber = selectedTerm.number
    for c in classList:
        calculateOverallMarkTerm(c.id, termNumber)
    
def countDetailTerm(term_id):
    finishLearning=[]
    notFinishLearning=[]
    finishPractising=[]
    notFinishPractising=[]
    finishAll=[]
    notFinishAll=[]
    
    selectedTerm = Term.objects.get(id=term_id)
    classList=Class.objects.filter(year_id=selectedTerm.year_id)
    
    for c in classList:
        number = TBHocKy.objects.filter(term_id=term_id,student_id__classes=c.id,hl_hk=None).count()
        if number==0:   finishLearning.append(c.name)
        else        :  notFinishLearning.append([c.name,number])
        
        if selectedTerm.number==1:        
            number = TBNam.objects.filter(year_id=selectedTerm.year_id,student_id__classes=c.id,term1=None).count()
            if number==0:  finishPractising.append(c.name)
            else        :  notFinishPractising.append([c.name,number])
        else:
            number = TBNam.objects.filter(year_id=selectedTerm.year_id,student_id__classes=c.id,term2=None).count()
            if number==0:  finishPractising.append(c.name)
            else        :  notFinishPractising.append([c.name,number])
                
        number = TBHocKy.objects.filter(term_id=term_id,student_id__classes=c.id,danh_hieu_hk=None).count()
        if number==0:  finishAll.append(c.name)
        else        :  notFinishAll.append([c.name,number])
    return  finishLearning,notFinishLearning,finishPractising,notFinishPractising,finishAll,notFinishAll       

#@transaction.commit_on_success                                                                                  
def finishTerm(request,term_id=None):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedTerm = Term.objects.get(id__exact = term_id)
    try:
        if in_school(request,selectedTerm.year_id.school_id) == False:
            return HttpResponseRedirect('/school')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

    if (get_position(request) != 4):
        return HttpResponseRedirect('/school')
    
    
    message=None
    
    if request.method == 'POST':
        if request.POST.get('finishTerm'):
            if request.POST['finishTerm']!=u'Khôi phục về trạng thái học kỳ trước':                
                request.user.userprofile.organization.status+=1 
            else:
                request.user.userprofile.organization.status=selectedTerm.number
                
            request.user.userprofile.organization.save()    
        if request.POST.get('tongKet'):
            finishTermInSchool(term_id)
            message="Đã tính tổng kết xong. Mời bạn xem kết quả phía dưới."
        
    
    selectedTerm= Term.objects.get(id=term_id)
    yearString=str(selectedTerm.year_id.time)+"-"+str(selectedTerm.year_id.time+1)
    
    finishLearning,notFinishLearning,finishPractising,notFinishPractising,finishAll,notFinishAll= countDetailTerm(term_id)
    
    hlList,pthlList = countTotalLearningInTerm(term_id)
    hkList,pthkList = countTotalPractisingInTerm(term_id)
    ddList,ptddList = countDanhHieuInTerm(term_id)

    currentTerm=get_current_term(request)            
    t = loader.get_template(os.path.join('school/finish','finish_term.html'))
        
    t2=time.time()
    print (t2-t1)
    c = RequestContext(request, {"message":message,
                                 "selectedTerm":selectedTerm,
                                 "currentTerm":currentTerm,
                                 "yearString":yearString,
                                 
                                 "finishLearning":finishLearning,
                                 "notFinishLearning":notFinishLearning,
                                 "finishPractising":finishPractising,
                                 "notFinishPractising":notFinishPractising,
                                 "finishAll":finishAll,
                                 "notFinishAll":notFinishAll,
                                 
                                 "hlList":hlList,
                                 "pthlList":pthlList,
                                 "hkList":hkList,
                                 "pthkList":pthkList,
                                 "ddList":ddList,
                                 "ptddList":ptddList,
                                }
                       )
    return HttpResponse(t.render(c))

def finishYearInSchool(year_id):
    
    classList=Class.objects.filter(year_id=year_id)
    for c in classList:
        calculateOverallMarkYear(c.id)
        xepLoaiLop(c.id)
        
def countDetailYear(year_id):
    finishLearning=[]
    notFinishLearning=[]
    finishPractising=[]
    notFinishPractising=[]
    finishAll=[]
    notFinishAll=[]
    
    classList=Class.objects.filter(year_id=year_id)
    
    for c in classList:
        
        number = TBNam.objects.filter(year_id=year_id,student_id__classes=c.id,hl_nam=None).count()
        if number==0:   finishLearning.append(c.name)
        else        :  notFinishLearning.append([c.name,number])
        
        number = TBNam.objects.filter(year_id=year_id,student_id__classes=c.id,year=None).count()
        if number==0:  finishPractising.append(c.name)
        else        :  notFinishPractising.append([c.name,number])
                
        number = TBNam.objects.filter(year_id=year_id,student_id__classes=c.id,danh_hieu_nam=None).count()
        if number==0:  finishAll.append(c.name)
        else        :  notFinishAll.append([c.name,number])

    return  finishLearning,notFinishLearning,finishPractising,notFinishPractising,finishAll,notFinishAll       

def finishYear(request,year_id):

    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedTerm=Term.objects.get(year_id=year_id,number=2)
    try:
        if in_school(request,selectedTerm.year_id.school_id) == False:
            return HttpResponseRedirect('/school')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

    if (get_position(request) != 4):
        return HttpResponseRedirect('/school')

    
    message=None
    if request.method == 'POST':
        if request.POST.get('finishTerm'):
           if request.POST['finishTerm']!=u'Khôi phục về học kỳ II':
                request.user.userprofile.organization.status=3
           else:
                request.user.userprofile.organization.status=2
                
           request.user.userprofile.organization.save()
        if request.POST.get('tongKet'):
            finishYearInSchool(year_id)
            
            message="Đã tính tổng kết xong. Mời bạn xem kết quả phía dưới."
    
    yearString=str(selectedTerm.year_id.time)+"-"+str(selectedTerm.year_id.time+1)
    finishLearning,notFinishLearning,finishPractising,notFinishPractising,finishAll,notFinishAll= countDetailYear(year_id)
    
    
    hkList,pthkList = countTotalPractisingInYear(year_id)
    hlList,pthlList = countTotalLearningInYear(year_id)
    ddList,ptddList = countDanhHieuInYear(year_id)
    
    currentTerm = get_current_term(request)
                    
    t = loader.get_template(os.path.join('school/finish','finish_year.html'))
    c = RequestContext(request, {"message":message,
                                     "currentTerm":currentTerm,
                                 "yearString":yearString,
                                 "finishLearning":finishLearning,
                                 "notFinishLearning":notFinishLearning,
                                 "finishPractising":finishPractising,
                                 "notFinishPractising":notFinishPractising,
                                 "finishAll":finishAll,
                                 "notFinishAll":notFinishAll,
                                 
                                 "hlList":hlList,
                                 "pthlList":pthlList,
                                 "hkList":hkList,
                                 "pthkList":pthkList,
                                 "ddList":ddList,
                                 "ptddList":ptddList,
                                }
                       )
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def thilai(request,class_id):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedClass = Class.objects.get(id__exact = class_id)
    try:
        if in_school(request,selectedClass.year_id.school_id) == False:
            return HttpResponseRedirect('/school')

    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

    ok=False
    position = get_position(request)
    if position ==4: ok=True
    #kiem tra xem giao vien nay co phai chu nhiem lop nay khong
    if position ==3:
        if selectedClass.teacher_id != None:
            if selectedClass.teacher_id.user_id.id == request.user.id:
                ok=True
                 
    if (not ok):
        return HttpResponseRedirect('/school')

    message=None
    tbNamList=TBNam.objects.filter(student_id__classes=class_id,thi_lai=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    tbMonList=[]
    aTKMonList=[]
    for tbNam in tbNamList:
        aTKMonList = TKMon.objects.filter(subject_id__class_id=class_id,student_id=tbNam.student_id,subject_id__primary__in=[0,1,2,3],current=True).order_by('subject_id__index','subject_id__name')
        for tbMon in aTKMonList:
            if tbMon.tb_nam==None: message="Chưa tổng kết xong điểm của cả lớp"
            
            elif (tbMon.tb_nam <5) & (tbMon.mg==False) :  
                tbMon.thi_lai=True
            else                                       :  
                tbMon.thi_lai=False
            
        tbMonList.append(aTKMonList)
        """
        if   tbNam.hl_thi_lai=='G'  : tbNam.hl_thi_lai='Giỏi'
        elif tbNam.hl_thi_lai=='K'  : tbNam.hl_thi_lai='Khá'
        elif tbNam.hl_thi_lai=='TB' : tbNam.hl_thi_lai='TB'
        elif tbNam.hl_thi_lai=='Y'  : tbNam.hl_thi_lai=u'Yếu'
        elif tbNam.hl_thi_lai=='Kem' : tbNam.hl_thi_lai='Kém'
        """
        
        
    vtMonChuyen = -1
    vtMonToan   = -1
    vtMonVan    = -1

    
    i=0    
    for tkMon in aTKMonList:
        if tkMon.subject_id.hs==3: vtMonChuyen =i
        if    tkMon.subject_id.name.lower().__contains__(u'toán'):
            vtMonToan=i
        elif  tkMon.subject_id.name.lower().__contains__(u'văn'):
            vtMonVan=i   
        i+=1     
    
    list= zip(tbMonList,tbNamList)
    
    if request.method =='POST':
        for aTKMonList,tbNam in list:
            sum=0
            sumFactor=0
            minMark=10
            monChuyen=None
                    
            for (i,tbMon) in enumerate(aTKMonList):
                if tbMon.thi_lai:
                    value = request.POST[str(tbMon.id)]
                    if len(value)!=0:
                        value1=float(value)
                        tbMon.diem_thi_lai=value1
                        tbMon.save()
                    else:
                        tbMon.diem_thi_lai=None
                        tbMon.save()
                ok=False    
                if tbMon.thi_lai:
                    if tbMon.diem_thi_lai!=None:
                        sumFactor+=tbMon.subject_id.hs
                        sum+=tbMon.diem_thi_lai*tbMon.subject_id.hs
                        if minMark>tbMon.diem_thi_lai:
                            minMark=tbMon.diem_thi_lai
                        ok=True
                if (not ok) & ( tbMon.mg==False ):
                    sumFactor+=tbMon.subject_id.hs
                    sum+=tbMon.tb_nam * tbMon.subject_id.hs
                    if minMark>tbMon.tb_nam:
                        minMark=tbMon.tb_nam
                        
                if   i==vtMonChuyen:
                    monChuyen=tbMon
                    
                if i==vtMonToan:
                    monToan=tbMon
                elif  i==vtMonVan:
                    monVan=tbMon                
            
            tbNam.tb_thi_lai=round(float(sum)/sumFactor,1)
            tbNam.hl_thi_lai=defineHlThiLai(tbNam.tb_thi_lai,monChuyen,monToan,monVan,minMark,)
            
            if (tbNam.hl_thi_lai!='Y') & (tbNam.hl_thi_lai!='Kem'):
                tbNam.len_lop=True
            else:
                tbNam.len_lop=False 
            tbNam.save()        
                                
    lengthList = len(list)
    if lengthList==0:
        message="Lớp chưa tổng kết xong hoặc không có học sinh nào phải thi lại"
    numberSubject= len(aTKMonList)
    
    yearString=str(selectedClass.year_id.time)+"-"+str(selectedClass.year_id.time+1)
    
    t = loader.get_template(os.path.join('school/finish','thi_lai.html'))
    t2=time.time()
    print (t2-t1)
    
    c = RequestContext(request, {"message":message,
                                 "selectedClass":selectedClass,
                                 "yearString":yearString,
                                 'lengthList':lengthList,
                                 'numberSubject':numberSubject,
                                 'aTKMonList':aTKMonList,
                                 'vtMonChuyen':vtMonChuyen,
                                 'vtMonToan':vtMonToan,
                                 'vtMonVan':vtMonVan,
                                 "list":list,
                                }
                       )
    

    return HttpResponse(t.render(c))
def updateHocLai(str):
    strs = str.split('*')
    if   (strs[0]=='0'):
        print "f1"
        id = int(strs[1])
        tkMon = TKMon.objects.get(id=id)
        
        if strs[2]!='-1':
            tkMon.thi_lai=True        
            tkMon.diem_thi_lai = float(strs[2])
        else:
            tkMon.thi_lai=False        
            tkMon.diem_thi_lai = None
                
        tkMon.save()
        
    elif (strs[0]=='1'):
        print "f2"
        id = int(strs[1])
        tbNam = TBNam.objects.get(id=id)
        
        if strs[2]!='-1':
            tbNam.tb_thi_lai=float(strs[2])
        else:  
            tbNam.tb_thi_lai=None    
        tbNam.save()
    else:    
        print "f3"
        id = int(strs[1])
        tbNam = TBNam.objects.get(id=id)

        if strs[2]!='-1':
            tbNam.hl_thi_lai=strs[2]
            if (strs[2]!='Y') & (strs[2]!='Kem'): 
                tbNam.len_lop=True
            else:                                 
                tbNam.len_lop=False
        else:
            tbNam.hl_thi_lai=None
            tbNam.len_lop=None
                 
        tbNam.save()
                                 
def saveHocLai(request):
    message = 'hello'
    if request.method == 'POST':

        str = request.POST['str']
        strs=str.split(':')
        print str
        length = len(strs)
        for i in range(1,length):
            updateHocLai(strs[i])
                                                            
        message='ok'
        data = simplejson.dumps({'message': message})
        return HttpResponse( data, mimetype = 'json')   

def renluyenthem(request,class_id):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedClass = Class.objects.get(id__exact = class_id)
    try:
        if in_school(request,selectedClass.year_id.school_id) == False:
            return HttpResponseRedirect('/school')

    except Exception as e:
        return HttpResponseRedirect(reverse('index'))

    ok=False
    position = get_position(request)
    if position ==4: ok=True
    #kiem tra xem giao vien nay co phai chu nhiem lop nay khong
    if position ==3:
        if selectedClass.teacher_id != None:
            if selectedClass.teacher_id.user_id.id == request.user.id:
                ok=True
                 
    if (not ok):
        return HttpResponseRedirect('/school')


    message=None
    hkList=TBNam.objects.filter(student_id__classes=class_id,ren_luyen_lai=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
    
    lengthList = len(hkList)
    if lengthList==0:
        message="Lớp chưa có hạnh kiểm cuối năm hoặc không có học sinh nào phải rèn luyện thêm"
    
    yearString=str(selectedClass.year_id.time)+"-"+str(selectedClass.year_id.time+1)
    
    print message
    t = loader.get_template(os.path.join('school/finish','ren_luyen_them.html'))
    t2=time.time()
    print (t2-t1)
    
    c = RequestContext(request, {"message":message,
                                 "selectedClass":selectedClass,
                                 "yearString":yearString,
                                 'lengthList':lengthList,
                                 "hkList":hkList,
                                }
                       )
    

    return HttpResponse(t.render(c))
	
def saveRenLuyenThem(request):
    message = 'hello'
    if request.method == 'POST':

        str  = request.POST['str']
        strs =str.split(':')
        print str
        id = int(strs[0])
        
        tbNam = TBNam.objects.get(id=id)
        if strs[1]!='No':
            tbNam.hk_ren_luyen_lai= strs[1]
        else:     
            tbNam.hk_ren_luyen_lai= None
        
        if strs[1]=='No':
            tbNam.len_lop=None
        elif strs[1]=='Y':
            tbNam.len_lop=False
        else:
            tbNam.len_lop=True       
            
        tbNam.save()                                                         
        message='ok'
        data = simplejson.dumps({'message': message})
        return HttpResponse( data, mimetype = 'json')   

def sendSMSResult(request,class_id,termNumber=None):
    t1=time.time()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect( reverse('login'))

    selectedClass = Class.objects.get(id__exact = class_id)
    
    try:
        if in_school(request,selectedClass.year_id.school_id) == False:
            return HttpResponseRedirect('/school')
    except Exception as e:
        return HttpResponseRedirect(reverse('index'))
    
    ok=False
    position = get_position(request)
    if position ==4: ok=True
    #kiem tra xem giao vien nay co phai chu nhiem lop nay khong
    if position ==3:
        if selectedClass.teacher_id != None:
            if selectedClass.teacher_id.user_id.id == request.user.id:
                ok=True
                 
    if (not ok):
        return HttpResponseRedirect('/school')
    if termNumber==None:
        currentTerm=get_current_term(request)
        termNumber = currentTerm.number 
                    
    message=None
    selectedYear  =selectedClass.year_id
    pupilList     =Pupil.objects.filter(classes=class_id,attend__is_member=True).order_by('index','first_name','last_name','birthday')    

    
    yearString = str(selectedYear.time)+"-"+str(selectedYear.time+1)
    tempList=[]
    list=[]
    # neu la hk1 hoac hk2
    termNumber=int(termNumber)
    
    if termNumber<3:
        tbHocKyList = TBHocKy.objects.filter(student_id__classes=class_id,term_id__number=termNumber).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        hkList      = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        hkList1 =[]
        if termNumber==1:
            for hk in hkList:
                hkList1.append(hk.term1)
        else:
            for hk in hkList:
                hkList1.append(hk.term2)
        list1=zip(pupilList,tbHocKyList,hkList1)        
    else:
        tbNamList = TBNam.objects.filter(student_id__classes=class_id).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday')
        list1=zip(pupilList,tbNamList,tbNamList)        

    contentList=[]            
    if termNumber<3:
        subjectList=Subject.objects.filter(class_id=class_id,primary__in=[0,termNumber,3,4]).order_by("index",'name')    
        markList = Mark.objects.filter(subject_id__class_id=class_id,term_id__number=termNumber,subject_id__primary__in=[0,termNumber,3,4],current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name')
        
        length = len(subjectList)    
        i=0    
        for m in markList:
            t= i % length
            if t ==0:
                markOfAPupil=[]
            if m.mg:
                  markOfAPupil.append("MG")
            elif m.tb==None:    
                  markOfAPupil.append("")
            elif subjectList[t].nx:
                markOfAPupil.append(convertMarkToCharacter1(m.tb))
            else:            
                markOfAPupil.append(m.tb)        
            
            if t==0:            
                tempList.append(markOfAPupil) 
            i+=1         
    else:
        idYear = selectedYear.id
        subjectList=Subject.objects.filter(class_id=class_id).order_by("index",'name')    
        markList   =TKMon.objects.filter(subject_id__class_id=class_id,current=True).order_by('student_id__index','student_id__first_name','student_id__last_name','student_id__birthday','subject_id__index','subject_id__name') 
        length = len(subjectList)

        i=0    
        for m in markList:
            t= i % length
            if t ==0:
                markOfAPupil=[]
                
            if m.mg:
                  markOfAPupil.append("MG")
            elif m.tb_nam==None:    
                  markOfAPupil.append("")
            elif subjectList[t].nx:
                markOfAPupil.append(convertMarkToCharacter1(m.tb_nam))
            else:                  
                markOfAPupil.append(m.tb_nam)        
            
            if t==0:            
                tempList.append(markOfAPupil) 
            i+=1
            
    i=1
    for p,tb,hk in list1:
        smsString=''
        markOfAPupil=tempList[i-1]
        for s,m in zip(subjectList,markOfAPupil):
            smsString+=to_en1(s.name)+':'+str(m)+', '
        if termNumber<3:    
            smsString+='TB:'+str(tb.tb_hk)+', '                
            smsString+='hoc luc :' + to_en1(convertHlToVietnamese(tb.hl_hk))+', '
            smsString+='hanh kiem:' + to_en1(convertHkToVietnamese(hk))
            if (tb.danh_hieu_hk=='G') | (tb.danh_hieu_hk=='TT') :
                smsString+=', '+'danh hieu:'+convertDanhHieu(tb.danh_hieu_hk)+'.'
            else:    
                smsString+='.'
        else:
            smsString+='TB:'+str(tb.tb_nam)+', '                
            smsString+='hoc luc :' + to_en1(convertHlToVietnamese(tb.hl_nam))+', '
            smsString+='hanh kiem:' + to_en1(convertHkToVietnamese(tb.year))+', '
            if (tb.danh_hieu_nam=='G') | (tb.danh_hieu_nam=='TT') :
                smsString+='danh hieu:'+convertDanhHieu(tb.danh_hieu_nam)+','
            smsString+='thuoc dien:'
            if  tb.len_lop==True:
                smsString+='len lop.'
            elif tb.len_lop==False:
                smsString+='khong len lop.'
            elif tb.thi_lai==True:
                smsString+='kiem tra lai mot so mon.'
            elif tb.ren_luyen_lai:
                smsString+='ren luyen them trong he.'
            else:
                smsString+='chua xep loai.'                            
        i+=1
        
        contentList.append(smsString)

    if termNumber < 3:    
        list=zip(pupilList,contentList,tbHocKyList)
    else:    
        list=zip(pupilList,contentList,tbNamList)
                        
    if request.method=="POST":
        data  = request.POST[u'data']
        datas = data.split('-')
        successString=''
        numberSent=0
        numberSuccess=0        
        i=1
        for p,c,tb in list:
            if str(i) in datas:   
                smsString = u'Tong ket '
                if termNumber==1:
                    termString=u'hoc ky I nam hoc '
                elif termNumber==2:
                    termString=u'hoc ky II nam hoc '
                else:
                    termString=u'ca nam nam hoc '        
                smsString+=termString+yearString
                smsString+=' cua hs '+to_en1(p.last_name)+' '+to_en1(p.first_name)+' nhu sau:'

                smsString+=c
                numberSent+=1
                if p.sms_phone:
                    sent=''
                    try:
                        sent=sendSMS(p.sms_phone,smsString,user)                        
                    except Exception as e:
                        pass
                    if sent=='1':
                        numberSuccess+=1
                        successString+=str(i)+'-'
                        tb.sent=True
                        tb.save()
            i+=1
            
        message="ok111111111111"  
        result ='Đã gửi thành công '+str(numberSuccess)+'/'+str(numberSent)  
        data = simplejson.dumps({'successString':successString,
                                 'result':result})
        return HttpResponse(data, mimetype = 'json')
                
    t = loader.get_template(os.path.join('school','send_sms_result.html'))

    t2=time.time()
    print (t2-t1)
    c = RequestContext(request, {"message":message, 
                                 "list":list,
                                 "selectedClass":selectedClass,
                                 "termNumber":termNumber,
                                 #"classList" :classList,
                                }
                       )
    

    return HttpResponse(t.render(c))
