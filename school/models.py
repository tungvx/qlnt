# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from app.models import *
#from viewMark import CHECKED_DATE
from datetime import datetime
CHECKED_DATE = datetime(2010,1,1,0,0,0)
import datetime

LOAI_CHOICES = ((0,u'Tính cả 2 kỳ'),(1,u'Chỉ tính kì 1'),(2,u'Chỉ tính kì 2'),(3,u'Cộng vào điểm TB(NN2)'),(4,u'Không tính điểm'))
SUBJECT_TYPES = (('-1',u'Chọn môn'),(u'Toán',u'Toán'),
                 (u'Vật lí', u'Vật lí'), (u'Hóa học', u'Hóa học'),
                 (u'Sinh học', u'Sinh học'),(u'Ngữ văn', u'Ngữ văn'),
                 (u'Lịch sử', u'Lịch sử'), (u'Địa lí', u'Địa lí'),
                 (u'Ngoại ngữ', u'Ngoại ngữ'), (u'GDCD',u'GDCD'),
                 (u'Công nghệ', u'Công nghệ'), (u'Thể dục', u'Thể dục'),
                 (u'Âm nhạc', u'Âm nhạc'),(u'Mĩ thuật', u'Mĩ thuật'),
                 (u'NN2', u'NN2'),(u'Tin học', u'Tin học'),
                 (u'GDQP-AN', u'GDQP-AN'))
SUBJECT_LIST = [u'Toán',u'Vật lí', u'Hóa học',u'Sinh học',u'Ngữ văn',
                u'Lịch sử', u'Địa lí', u'Ngoại ngữ', u'GDCD',u'Công nghệ',
                u'Thể dục', u'Âm nhạc',u'Mĩ thuật',u'NN2',u'Tin học', u'GDQP-AN']
SUBJECT_LIST_ASCII = [u'toan',u'vat li', u'hoa hoc',u'sinh hoc',u'ngu van',
                u'lich su', u'dia li', u'ngoai ngu', u'gdcd',u'cong nghe',
                u'the duc', u'am nhac',u'mi thuat',u'nn2',u'tin hoc', u'gdqp-an']
GENDER_CHOICES = ((u'Nam', u'Nam'),(u'Nữ', u'Nữ'),)
TERM_CHOICES = ((1, u'1'), (2, u'2'),(3, u'3'),)
HK_CHOICES = ((u'T', u'Tốt'), (u'K', u'Khá'),(u'TB',u'Trung Bình'),(u'Y', u'Yếu'),)
HL_CHOICES = ((u'G', u'Giỏi'), (u'K', u'Khá'),(u'TB',u'Trung Bình'),(u'Y', u'Yếu'),(u'Kem', u'Kém'))
#k co nghia la khong duoc danh hieu gi
DH_CHOICES = ((u'XS', u'Học sinh xuất sắc'),(u'G', u'Hoc sinh giỏi'), (u'TT', u'Học sinh tiên tiến'),(u'K',u'Không được gì'))
KT_CHOICES = ((u'Khen trước lớp',u'Khen trước lớp'), (u'Khen trước toàn trường',u'Khen trước toàn trường'),
              (u'Được tặng danh hiệu học sinh khá',u'Được tặng danh hiệu học sinh khá'), 
              (u'Được tặng danh hiệu học sinh giỏi',u'Được tặng danh hiệu học sinh giỏi'), (u'Được ghi tên vào bảng danh dự của trường',u'Được ghi tên vào bảng danh dự của trường'), 
              (u'Được tặng danh hiệu học sinh xuất sắc',u'Được tặng danh hiệu học sinh xuất sắc'), (u'Được khen thưởng đặc biệt',u'Được khen thưởng đặc biệt'))
KL_CHOICES = ((u'Khiển trách trước lớp',u'Khiển trách trước lớp'), (u'Khiển trách trước hội đồng kỷ luật',u'Khiển trách trước hội đồng kỷ luật'), 
              (u'Cảnh cáo trước toàn trường',u'Cảnh cáo trước toàn trường'), (u'Đình chỉ học',u'Đình chỉ học'))
SCHOOL_LEVEL_CHOICE = ((1, u'1'), (2, u'2'), (3, u'3'))
DIEM_DANH_TYPE = ((u'Có phép', u'Có phép'),(u'Không phép', u'Không phép'),(u'k','Đi học'))
BAN_CHOICE = ((u'KHTN',u'Ban KHTN'),(u'KHXH',u'Ban KHXH-NV'),(u'CBA',u'Ban Cơ bản A'),
              (u'CBB',u'Ban Cơ bản B'),(u'CBB',u'Ban Cơ bản C'),
              (u'CBD',u'Ban Cơ bản D'),(u'CB',u'Ban Cơ bản'))
KHOI_CHOICE=((1,u'Khối 1'),(2,u'Khối 2'),(3,u'Khối 3'),(4,u'Khối 4'),(5,u'Khối 5'),(6,u'Khối 6'),(7,u'Khối 7'),             
            (8,u'Khối 8'),(9,u'Khối 9'),(10,u'Khối 10'),(11,u'Khối 11'),(12,u'Khối 12'))            
KV_CHOICE =((u'1',u'KV1'),(u'2A','KV2'),(u'2B','KV2-NT'),(u'3',u'KV3'))
DT_CHOICE = ((1,u'Kinh (Việt)'),(2,u'Tày'),(3,u'Nùng'),(4,u'Hmông (Mèo)'),(5,u'Mường'),(6,u'Dao'),(7,u'Khmer'),
            (8,u'Êđê'),(9,u'CaoLan'),(10,u'Thái'),(11,u'Gia rai'),(12,u'La chư'),(13,u'Hà nhì'),(14,u'Giáy'),
            (15,u"M'nông"),(16,u'Cơ tu'),(17,u'Xê đăng'),(18,u"X'tiêng"),(19,u"Ba na"),(20,"H'rê"),(21,u'Giê-Triêng'),
            (22,u'Chăm'),(23,u'Cơ ho'),(24,u'Mạ'),(25,u'Sán Dìu'),(26,u'Thổ'),(27,u'Khơ mú'),(28,u'Bru - Vân Kiều'),
            (29,u'Tà ôi'),(30,u'Co'),(31,u'Lào'),(32,u'Xinh mun'),(33,u'Chu ru'),(35,u'Phù lá'),(36,u'La hú'),(37,u'Kháng'),
            (38,u'Lự'),(39,u'Pà Thén'),(40,u'Lô lô'),(41,u'Chứt'),(42,u'Mảng'),(43,u'Cơ lao'),(44,u'Bố y'),(45,u'La ha'),
            (46,u'Cống'),(47,u'Ngái'),(48,u'Si la'),(49,u'Pu Péo'),(50,u'Brâu'),(51,u'Rơ măm'),(52,u'Ơ đu'),(53,u'Hoa'),
            (54,u'Raglay'),(55,u'HMông'),(56,u'Pacô'),(57,u'Pahy'),(60,u'Jơ lơng'),(61,u'Rơ ngao'),(62,u'Ra dong'),
            (63,u'Sơ rá'),(64,u'Jẻ'),(65,u'Mơ nâm'),(66,u'Hơ lăng'),(67,u'Hoa (Hán)'),(68,u'Sán chay'),
            (69,u'CaDong'),(70,u'Chơ ro'))
LENLOP_CHOICES=((True,u'Được lên lớp'),(False,u'Không được lên lớp'))
SCHOOL_ACTION_STATUS=((0, u'Trường mới'),(1, u'Đang học kì 1'), (2, u'Đang học kì 2'), (3, u'Đang nghỉ hè'))
CLASS_ACTION_STATUS=((1, u'Đang học kì 1'), (2, u'Đang học kì 2'), (3, u'Đang nghỉ hè'))
ACTIVE_CHOICES=((True,u'Đang diễn ra'),(False,u'Đã kết thúc'))

DAY_CHOICE =((2, u'Thu 2'), (2, u'Thu 2'), (3, u'Thu 3'), (4, u'Thu 4'), (5, u'Thu 5'), (6, u'Thu 6'), (7, u'Thu 7'))

def this_year():
    return int(date.today().year)

#validate mark of pupil
#mark must be between 0 and 10

def validate_class_label(value):
    if not value.strip(): raise ValidationError(u'Bạn chưa nhập danh sách tên lớp ')

def validate_mark(value):
    if value < 0 or value > 10:
        raise ValidationError(u'Điểm phải nằm trong khoảng từ 0 đến 10')

#validate the phone format
def validate_phone(value):
    if len(value) <= 5:
        raise ValidationError(u'Điện thoạt phải có trên 5 chữ số')
    try:
        int(value)
    except ValueError:
        raise ValidationError(u'Không đúng định dạng')

#validate birthday. set range between 1990 and current year
def validate_birthday(value):
    if value < date(1900,1,1) or value > date.today():
        raise ValidationError(u'Ngày nằm ngoài khoảng cho phép')

#validate the year that pupil go to class 1. Ragne between 1990 and this year
def validate_year(value):
    if value < 1990 or value > date.today().year:
        raise ValidationError(u'Năm nằm ngoài khoảng cho phép')

#validate the date that pupil join school
def validate_join_date(value):
    if value < date(1990,1,1) or value > date.today():
        raise ValidationError(u'Ngày nằm ngoài khoảng cho phép')

def validate_dd_date(value):
    if value > date.today():
        raise ValidationError(u'Ngày nẳm ngoài khoảng cho phép')
#validate he so diem cua mon    
def validate_hs(value):
    #he so bang 0 la cho nhung mon cham diem bang nhan xet
    if value < 0:
        raise ValidationError(u'Hệ số không được nhỏ hơn 0')
    if value > 3:
        raise ValidationError(u'Hệ số không được lớn hơn 3')

def validate_join_mark(value):
    if value <= 0:
        raise ValidationError(u'Điểm nhập trường phải lớn hơn 0')
    if value >= 55:
        raise ValidationError(u'Điểm nhập trường phải nhỏ hơn 55')

def validate_hs_luong(value):
    if value <= 0 or value > 13:
        raise ValidationError(u'Hệ số nằm ngoài khoảng cho phép')
    
def validate_muc_luong(value):
    if value <= 0:
        raise ValidationError(u'Mức lương phải lớn hơn 0')

def validate_num(value):
    try:
        int(value)
    except :
        raise ValidationError(u'Định dạng không đúng')


def log_action(request, object, change_message):
    """
    Log an entry to Django admin's log
    """
    from django.contrib.admin.models import LogEntry
    from django.contrib.contenttypes.models import ContentType

    LogEntry.objects.log_action(
        user_id         = request.user.id,
        content_type_id = ContentType.objects.get_for_model(object).pk,
        object_id       = object.pk,
        object_repr     = change_message, # Message you want to show in admin action list
        change_message  = "app-log", # I used same
        action_flag     = 4
    )


class DanhSachLoaiLop(models.Model):
    loai = models.CharField("Loại", max_length = 15)
    school_id = models.ForeignKey(Organization,verbose_name = "Trường")
    
    class Meta:
        verbose_name = "Danh sách loại lớp"
        verbose_name_plural = "Danh sách loại lớp"
        
    def __unicode__(self):
        return self.loai

    #cac khoi trong 1 truong    
class Block(models.Model):
    number = models.SmallIntegerField("Khối(*)", max_length = 2, choices=KHOI_CHOICE)
    school_id = models.ForeignKey(Organization, verbose_name = "Trường(*)")

    def TkDh(self, request):
        so_luong  =[0,0,0,0]
        phan_tram =[0,0,0,0]
        sum=0.0

        classList = Class.objects.filter(block_id=self.id ,year_id=int(request.session.get('year_id')))

        for c in classList:
            so_luong_c, phan_tram_c, sum_c = c.TkDh(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)

    def TkHk(self, request):
        so_luong  =[0,0,0,0,0]
        phan_tram =[0,0,0,0,0]
        sum=0.0

        classList = Class.objects.filter(block_id=self.id ,year_id=int(request.session.get('year_id')))

        for c in classList:
            so_luong_c, phan_tram_c, sum_c = c.TkHk(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)

    def TkHl(self, request):
        so_luong  =[0,0,0,0,0,0]
        phan_tram =[0,0,0,0,0,0]
        sum=0.0

        classList = Class.objects.filter(block_id=self.id ,year_id=int(request.session.get('year_id')))

        for c in classList:
            so_luong_c, phan_tram_c, sum_c = c.TkHl(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)
        
    class Meta:
        verbose_name = "Khối"
        verbose_name_plural = "Khối"

    def __unicode__(self):
        return str(self.number)

class Team(models.Model):
    name = models.CharField("Tổ", max_length= 30)
    school_id = models.ForeignKey(Organization, verbose_name="Trường(*)")

    class Meta:
        verbose_name = "Tổ"
        verbose_name_plural = "Tổ"

    def __unicode__(self):
        return unicode(self.name)

class Group(models.Model):
    name = models.CharField("Nhóm", max_length= 30)
    team_id = models.ForeignKey(Team, verbose_name="Tổ(*)")

    class Meta:
        verbose_name = "Nhóm"
        verbose_name_plural = "Nhóm"

    def __unicode__(self):
        return unicode(self.name)

class BasicPersonInfo(models.Model):
    last_name = models.CharField("Họ", max_length = 35, blank = True) # tach ra first_name and last_name de sort va import from excel file
    first_name = models.CharField("Tên(*)", max_length = 55)#vi phan nhap bang tay, ho ten se dc luu vao first_name nen max_length phai dc tang len gap doi
    birthday = models.DateField("Ngày sinh(*)", null = True, validators = [validate_birthday])
    birth_place = models.CharField("Nơi sinh", max_length = 200, blank = True)
    dan_toc = models.CharField("Dân tộc", max_length = 15, blank = True, default = 'Kinh')
    ton_giao = models.CharField("Tôn giáo", max_length = 20, blank = True)
    quoc_tich = models.CharField("Quốc tịch", max_length = 20, blank = True, default = 'Việt Nam')
    home_town = models.CharField("Quê quán", max_length = 100, blank = True) #nguyen quan
    sex = models.CharField("Giới tính(*)", max_length = 3, choices = GENDER_CHOICES, default = 'Nam')
    phone = models.CharField("Điện thoại", max_length = 15, blank = True, validators = [validate_phone])
    sms_phone = models.CharField("Điện thoại nhận tin nhắn", max_length = 15, blank = True, validators = [validate_phone])
    current_address = models.CharField("Địa chỉ", max_length = 200, blank = True)
    email = models.EmailField("Email", null = True, blank = True)
    index = models.IntegerField("Số thứ tự(*)", default=0)
    note = models.TextField("Ghi chú", blank= True)
    class Meta:
        abstract = True
    
    def full_name(self):
        return ' '.join([self.last_name, self.first_name])
    
    def __unicode__(self):
        return self.last_name + " " + self.first_name
        
    #class Admin: pass

class Teacher(BasicPersonInfo):
    major = models.CharField("Dạy môn(*)", max_length=45, default='-1', choices=SUBJECT_TYPES)
    user_id = models.OneToOneField(User, verbose_name = "Tài khoản")
    school_id = models.ForeignKey(Organization, verbose_name = "Trường")
    group_id = models.ForeignKey(Group, null=True, blank=True, verbose_name="Nhóm", on_delete = models.SET_NULL)
    team_id = models.ForeignKey(Team, null=True, blank=True, verbose_name="Tổ", on_delete = models.SET_NULL)
    cmt = models.CharField("Chứng minh thư", null=True, blank=True, max_length=10, validators=[validate_num])
    ngay_cap = models.DateField("Ngày cấp", null=True, blank=True, validators=[validate_dd_date])
    noi_cap = models.CharField("Nơi cấp", null=True, blank=True, max_length=30)
    ngay_vao_doan = models.DateField("Ngày vào đoàn", null=True, blank=True, validators=[validate_dd_date])
    ngay_vao_dang = models.DateField("Ngày vào đảng", null=True, blank=True, validators=[validate_dd_date])
    muc_luong = models.IntegerField("Mức lương", null=True, blank=True, validators=[validate_muc_luong])
    hs_luong = models.FloatField("Hệ số lương", null=True, blank=True, validators=[validate_hs_luong])
    bhxh = models.CharField("Số bảo hiểm xã hội", null=True, blank=True, max_length=10, validators=[validate_num])

    def teaching_class(self):
        classes = Class.objects.filter(teacher_id = self)
        if classes:
            return classes[0]
        else:
            return None

    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Giáo viên"
        unique_together = ("school_id", "first_name", "last_name", "birthday",)

class Year(models.Model):
    time = models.IntegerField("Năm", max_length = 4, validators = [validate_year]) # date field but just use Year
    school_id = models.ForeignKey(Organization, verbose_name = "Trường")

    def TkDh(self, request):
        so_luong  =[0,0,0,0]
        phan_tram =[0,0,0,0]
        sum=0.0

        blockList = Block.objects.filter(school_id=self.school_id)

        for c in blockList:
            so_luong_c, phan_tram_c, sum_c = c.TkDh(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)

    def TkHk(self, request):
        so_luong  =[0,0,0,0,0]
        phan_tram =[0,0,0,0,0]
        sum=0.0

        blockList = Block.objects.filter(school_id=self.school_id)

        for c in blockList:
            so_luong_c, phan_tram_c, sum_c = c.TkHk(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)

    def TkHl(self, request):
        so_luong  =[0,0,0,0,0,0]
        phan_tram =[0,0,0,0,0,0]
        sum=0.0

        blockList = Block.objects.filter(school_id=self.school_id)

        for c in blockList:
            so_luong_c, phan_tram_c, sum_c = c.TkHl(request)
            for i in range(len(so_luong_c)):
                so_luong[i] += so_luong_c[i]
            sum += sum_c

        if sum!=0:
            for i in range(len(so_luong)):
                phan_tram[i]=so_luong[i]/sum *100

        return so_luong, phan_tram, int(sum)
    
    class Meta:
        verbose_name = "Năm học"
        verbose_name_plural = "Năm học"
    
    def __unicode__(self):
        return str(self.time) + "-" + str(self.time+1)
        
class StartYear(models.Model):
    time = models.IntegerField("Năm", max_length = 4, validators = [validate_year]) # date field but just use Year
    school_id = models.ForeignKey(Organization)
    
    
    class Meta:
        verbose_name = "Khóa"
        verbose_name_plural = "Khóa"
        
    def __unicode__(self):
        return str(self.time)
    
class Term(models.Model):
    number = models.IntegerField("Kì", max_length=1, choices = TERM_CHOICES)
    # neu active =false thi khong cho phep sua diem nua
    year_id = models.ForeignKey(Year, verbose_name = "Năm học")
    
    class Meta:
        verbose_name = "Kì"
        verbose_name_plural = "Kì"
        
    def __unicode__(self):
        return str(self.number) + " " + str(self.year_id)         
    #class Admin: pass

class Class(models.Model):
    name = models.CharField("Tên lớp(*)", max_length = 20)
    index = models.IntegerField("Số thứ tự", default=0)
    phan_ban = models.CharField("Phân ban", max_length=5, choices= BAN_CHOICE, default=u'CB', null = True)
    max = models.IntegerField("Max student index", default=0, null = True)
    status = models.SmallIntegerField("Tình trạng", max_length = 3, null = True, blank= True, choices = CLASS_ACTION_STATUS)


    year_id = models.ForeignKey(Year, verbose_name = "Năm học(*)")
    #lop nay thuoc khoi nao
    block_id = models.ForeignKey(Block, verbose_name = "Khối(*)")
    teacher_id = models.OneToOneField(Teacher, verbose_name = "Giáo viên chủ nhiệm", null = True, blank = True) #field nay chi dung de phan quyen, vi vay chi gan 1 gia tri nhan dang


    def get_term(self, request):
        if int(request.session.get('term_number')) == 1:
            return 'HỌC KỲ I'
        elif int(request.session.get('term_number')) == 2:
            return 'HỌC KỲ II'
        else:
            return 'CẢ NĂM'

    def TkDh(self, request):
        if int(request.session.get('term_number')) < 3:
            return self.TkDhKy(request)
        else:
            return self.TkDhNam()

    def TkHk(self, request):
        if int(request.session.get('term_number')) < 3:
            return self.TkHkKy(request)
        else:
            return self.TkHkNam()

    def TkHl(self, request):
        if int(request.session.get('term_number')) < 3:
            return self.TkHlKy(request)
        else:
            return self.TkHlNam()

    def TkDhNam(self):
        slList=[0,0,0,0]
        ptList=[0,0,0,0]

        slList[0]=TBNam.objects.filter(student_id__classes=self.id,danh_hieu_nam='G').count()
        slList[1]=TBNam.objects.filter(student_id__classes=self.id,danh_hieu_nam='TT').count()
        slList[3]=TBNam.objects.filter(student_id__classes=self.id,danh_hieu_nam=None).count()
        #slList[2]=
        #slList[2]=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,len_lop=True).count()
        #slList[3]=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,len_lop=False).count()
        #slList[4]=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,thi_lai=True).count()
        #slList[5]=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,ren_luyen_lai=True).count()
        #sl1=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,len_lop=True).count()
        #sl2=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,len_lop=False).count()
        #sl3=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,thi_lai=True).count()
        #sl4=TBNam.objects.filter(year_id=year_id,student_id__classes=class_id,ren_luyen_lai=True).count()
        sum = Pupil.objects.filter(classes=self.id,attend__is_member=True).count()

        #slList[2] = sum-sl1-sl2-sl3-sl4

        if (sum!=0):
            for i in range(3):
                ptList[i]=float(slList[i])/sum *100

        return slList,ptList,int(sum)

    def TkHkNam(self):
        slList  =[0,0,0,0,0]
        ptslList=[0,0,0,0,0]
        sum=0.0
        string=['T','K','TB','Y',None]
        for i in range(string.__len__()):
            slList[i]=TBNam.objects.filter(student_id__classes=self,year=string[i]).count()
            sum+=slList[i]
        if sum!=0:
            for i in range(string.__len__()):
                ptslList[i]=slList[i]/sum *100

        return slList,ptslList,int(sum)

    def TkHlNam(self):
        slList  =[0,0,0,0,0,0]
        ptslList=[0,0,0,0,0,0]
        sum=0.0
        string=['G','K','TB','Y','Kem',None]
        for i in range(string.__len__()):
            slList[i]=TBNam.objects.filter(student_id__classes=self.id,hl_nam=string[i]).count()
            sum+=slList[i]
        if sum!=0:
            for i in range(string.__len__()):
                ptslList[i]=slList[i]/sum *100

        return slList,ptslList,int(sum)

    def TkDhKy(self,request):
        slList  =[0,0,0,0]
        ptslList=[0,0,0,0]
        sum=0.0
        string=['G','TT','K',None]
        for i in range(string.__len__()):
            slList[i]=TBHocKy.objects.filter(term_id=int(request.session.get('term_id')),student_id__classes=self.id,danh_hieu_hk=string[i]).count()
            sum+=slList[i]
        if sum!=0:
            for i in range(string.__len__()):
                ptslList[i]=slList[i]/sum *100

        return slList,ptslList ,int(sum)

    def TkHkKy(self, request):
        slList  =[0,0,0,0,0]
        ptslList=[0,0,0,0,0]
        sum=0.0

        string=['T','K','TB','Y',None]
        selectedTerm = Term.objects.get(id=int(request.session.get('term_id')))
        year_id = selectedTerm.year_id
        if selectedTerm.number ==1:
            for i in range(string.__len__()):
                slList[i]=TBNam.objects.filter(year_id=year_id,student_id__classes=self.id,term1=string[i]).count()
                sum+=slList[i]
        else:
            for i in range(string.__len__()):
                slList[i]=TBNam.objects.filter(year_id=year_id,student_id__classes=self.id,term2=string[i]).count()
                sum+=slList[i]

        if sum!=0:
            for i in range(string.__len__()):
                ptslList[i]=slList[i]/sum *100

        return slList,ptslList,int(sum)

    def TkHlKy(self, request):
        slList  =[0,0,0,0,0,0]
        ptslList=[0,0,0,0,0,0]
        sum=0.0
        string=['G','K','TB','Y','Kem',None]
        for i in range(string.__len__()):
            slList[i]=TBHocKy.objects.filter(term_id__id=int(request.session.get('term_id')),hl_hk=string[i],student_id__classes=self.id).count()
            sum+=slList[i]
        if sum!=0:
            for i in range(string.__len__()):
                ptslList[i]=slList[i]/sum *100

        return slList,ptslList,int(sum)

    def teacher(self):
        if self.teacher_id:
            return unicode(self.teacher_id)
        else:
            return None
    def strip_name(self):
        return self.name.lower().replace(' ', '')
    
    def __unicode__(self):
        return self.name

    def attended_student(self):
        students = self.student_set.all()
        return students

    #this function will return list of students those are studying in this class
    def students(self):
        return self.student_set.filter(attend__is_member = True)


    def number_of_pupils(self):
        try:
            return self.students().count()
        except Exception :
            return 0

        

    class Meta:
        verbose_name = "Lớp"
        verbose_name_plural = "Lớp"
        unique_together = ("year_id", "name")
    #class Admin: pass
        
class Pupil(BasicPersonInfo):
    year = models.IntegerField("Năm học lớp 1", validators = [validate_year], blank = True, null = True) #year that pupil go to class 1

    school_join_date = models.DateField("Ngày nhập trường(*)", default = date.today(),validators=[validate_join_date])
    ban_dk = models.CharField("Ban đăng kí(*)", max_length = 5, choices = BAN_CHOICE, default = u'CB')
    school_join_mark = models.IntegerField("Điểm tuyển sinh", null = True, blank = True, validators = [validate_join_mark])
    #thong tin ca nhan
    khu_vuc = models.CharField("Khu vực", max_length = 3, choices = KV_CHOICE, blank = True)
    doi = models.BooleanField("Là đội viên", blank = True, default = False)
    ngay_vao_doi = models.DateField("Ngày vào đội", blank = True, null = True, validators=[validate_dd_date])
    doan = models.BooleanField("Là đoàn viên", blank = True, default = False)
    ngay_vao_doan = models.DateField("Ngày vào đoàn", blank = True, null = True, validators=[validate_dd_date])
    dang = models.BooleanField("Là đảng viên", blank = True, default = False)
    ngay_vao_dang = models.DateField("Ngày vào đảng", blank = True, null = True, validators=[validate_dd_date])
    uu_tien = models.CharField("Ưu tiên", blank = True, max_length = 100)
    
    #thong tin gia dinh
    father_name = models.CharField("Họ và tên bố", max_length = 45, blank = True)
    father_birthday = models.DateField("Ngày sinh của bố", null = True, blank = True, validators = [validate_birthday])
    father_phone = models.CharField("Điện thoại của bố", max_length = 15, null = True, blank = True, validators = [validate_phone])
    father_job = models.CharField("Nghê nghiệp của bố", max_length = 100, blank = True)
    mother_name = models.CharField("Họ và tên mẹ", max_length = 45, blank = True)
    mother_birthday = models.DateField("Ngày sinh của mẹ", null = True, blank = True, validators = [validate_birthday])
    mother_job = models.CharField("Nghê nghiệp của mẹ", max_length = 100, blank = True)    
    mother_phone = models.CharField("Điện thoại của mẹ", max_length = 15, null = True, blank = True, validators = [validate_phone])
    
    current_status = models.CharField("Tình trạng", max_length = 200, blank = True, null = True, default = 'OK')
    disable = models.BooleanField("Không còn trong trường", default = False)
    
    user_id = models.OneToOneField(User, verbose_name = "tài khoản", null = True, blank = True) # nullable is temporary 
    start_year_id = models.ForeignKey(StartYear, verbose_name = "khóa")
    class_id = models.ForeignKey(Class, verbose_name = "lớp", null = True, blank = True)
    school_id = models.ForeignKey(Organization, verbose_name = "trường", null = True, blank = True)
    classes = models.ManyToManyField(Class, through="Attend", related_name='student_set')

    def thuoc_dien(self, request):
        if int(request.session.get('termNumber')) == 1:
            return ''
        tbNam = TBNam.objects.filter(student_id__id = self.id, student_id__classes = int(request.session.get('class_id')))[0]
        if   tbNam.len_lop:
            return 'Thuộc diện: Được lên lớp.'
        elif tbNam.len_lop == False:
            return 'Thuộc diện: Không được lên lớp.'
        elif tbNam.thi_lai:
            return 'Thuộc diện: kiểm tra lại trong hè.'
        elif tbNam.ren_luyen_lai:
            return 'Thuộc diện: rèn luyện thêm trong hè.'
        else:
            return 'Thuộc diện: Chưa được xếp loại.'

    def get_tbNam(self, request):
        tbNam = TBNam.objects.filter(student_id__id = self.id, student_id__classes = int(request.session.get('class_id')))[0]
        if request.session.get('termNumber') == '1':
            return tbNam.term1
        elif request.session.get('termNumber') == '2':
            return tbNam.term2
        else:
            return tbNam.year

    def get_tkDiemDanh(self, request):
        return TKDiemDanh.objects.filter(student_id__id = self.id, student_id__classes=int(request.session.get('class_id')),term_id__number=int(request.session.get('termNumber')))[0]

    def get_tbHocky(self, request):
        return TBHocKy.objects.filter(student_id__id = self.id, student_id__classes=int(request.session.get('class_id')),term_id__number=int(request.session.get('termNumber')))[0]

    def get_attended_classes(self):
        classes = Class.objects.filter(pupil__id=self.id)
        return classes

    def get_attended(self):
        attended = Attend.objects.filter(pupil__id=self.id)
        return attended

    def current_class(self):
        attends = Attend.objects.filter(pupil=self, leave_time=None)
        if not attends:
            #print classes
            #raise Exception('InvalidClassSet_%s' % self.id)
            pass
        else:
            return attends[0]._class

    def join_class(self, _class, time = None):
        if not time:
            time = date.today()
        current = self.current_class()
        try:
            if current:
                relationship = Attend.objects.filter(pupil=self, _class=current, leave_time=None)
                if len(relationship) == 1:
                    if current != _class:
                        relationship[0].leave_time = date.today()
                        relationship[0].is_member = False
                        relationship[0].save()
                        Attend.objects.create(pupil = self,
                                              _class = _class,
                                              attend_time = time,
                                              leave_time = None )
                        self.index = _class.max + 1
                        _class.max += 1
                        _class.save()
                        self.class_id = _class
                        self.save()
                elif not relationship:
                    Attend.objects.create(pupil = self,
                                          _class = _class,
                                          attend_time = time,
                                          leave_time = None )
                    self.class_id = _class
                    self.index = _class.max + 1
                    _class.max += 1
                    _class.save()
                    self.save()
                else:
                    print relationship
                    raise Exception(u'InvalidClassSet_%s' % self.id)
            else:
                #this only use for converting from 1n to nm
                #TODO delete this section after removing class_id
                Attend.objects.create(pupil = self,
                                      _class = _class,
                                      attend_time = time,
                                      leave_time = None )
                self.class_id = _class
                self.index = _class.max + 1
                _class.max += 1
                _class.save()
                self.save()
            return self
        except Exception as e:
            print e
            raise e
    def get_school(self):
        return self.school_id

    class Meta:
        verbose_name = "Học sinh"
        verbose_name_plural = "Học sinh"
        unique_together = ("class_id", "first_name", "last_name", "birthday",)

class Attend(models.Model):
    pupil = models.ForeignKey(Pupil, verbose_name=u"Học sinh")
    _class = models.ForeignKey(Class, verbose_name=u"Lớp")
    attend_time = models.DateTimeField("Thời gian nhập lớp")
    leave_time = models.DateTimeField("Thời gian rời lớp", null = True)
    is_member = models.BooleanField("Học xong lớp", default= True) #this field take value True when student is
                                                                    #member of this class that attend class till the end
    def get_class(self):
        return self._class

    def history_check(self):
        mark = self.pupil.mark_set.all()
        for m in mark:
            if not m.current:
                if m.subject_id.class_id == self._class:
                    return True
        return False

    def __unicode__(self):
        return unicode(self.pupil) + '_' + unicode(self._class)

class Subject(models.Model):    
    name = models.CharField("Tên môn học(*)", max_length = 45) # can't be null
    type = models.CharField("Môn(*)", max_length=45, default='', choices= SUBJECT_TYPES)
    hs = models.FloatField("Hệ số(*)", validators = [validate_hs])
    nx = models.BooleanField("Là môn nhận xét", default= False)

    primary = models.SmallIntegerField("Tính điểm(*)", default = 0, choices = LOAI_CHOICES)
    index = models.IntegerField("Số thứ tự(*)", default=0)

    number_lesson = models.IntegerField("So Tiet", default = 0)
    current_lesson = models.IntegerField("Tiet hoc hien tai", default=0)
    class_id = models.ForeignKey(Class, verbose_name = "Lớp(*)")    
    teacher_id = models.ForeignKey(Teacher, verbose_name = "Giáo viên", null= True ) # field nay de cung cap permission cho giao vien de nhap diem
    
    class Meta:
        verbose_name = "Môn"
        verbose_name_plural = "Môn"
        unique_together = ("name", "class_id")
    
    def __unicode__(self):
        return self.name

    def strip_name(self):
        return self.name.lower().replace(' ', '')
    def get_primary(self):
        return LOAI_CHOICES[self.primary][1].encode("UTF-8")
    
    #class Admin: pass

class Mark(models.Model):
    
    mieng_1 = models.FloatField("Điểm miệng 1", null = True, blank = True, validators = [validate_mark])
    mieng_2 = models.FloatField("Điểm miệng 2", null = True, blank = True, validators = [validate_mark])
    mieng_3 = models.FloatField("Điểm miệng 3", null = True, blank = True, validators = [validate_mark])
    mieng_4 = models.FloatField("Điểm miệng 4", null = True, blank = True, validators = [validate_mark])
    mieng_5 = models.FloatField("Điểm miệng 5", null = True, blank = True, validators = [validate_mark])
    mlam_1 = models.FloatField("Điểm 15' 1", null = True, blank = True, validators = [validate_mark])
    mlam_2 = models.FloatField("Điểm 15' 2", null = True, blank = True, validators = [validate_mark])
    mlam_3 = models.FloatField("Điểm 15' 3", null = True, blank = True, validators = [validate_mark])
    mlam_4 = models.FloatField("Điểm 15' 4", null = True, blank = True, validators = [validate_mark])
    mlam_5 = models.FloatField("Điểm 15' 5", null = True, blank = True, validators = [validate_mark])
    mot_tiet_1 = models.FloatField("Điểm 1 tiết 1", null = True, blank = True, validators = [validate_mark])
    mot_tiet_2 = models.FloatField("Điểm 1 tiết 2", null = True, blank = True, validators = [validate_mark])
    mot_tiet_3 = models.FloatField("Điểm 1 tiết 3", null = True, blank = True, validators = [validate_mark])
    mot_tiet_4 = models.FloatField("Điểm 1 tiết 4", null = True, blank = True, validators = [validate_mark])
    mot_tiet_5 = models.FloatField("Điểm 1 tiết 5", null = True, blank = True, validators = [validate_mark])
    
    diem   = models.CharField("điểm", null = True, blank = True, default = '||', max_length=100)
    sent   = models.CharField("Đã gửi",null = True,blank = True, default = '||||', max_length=50)
    time   = models.CharField("Thời gian tạo",null = True, blank=True, default='||||', max_length=200)

    ck = models.FloatField("Điểm thi cuối kì", null = True, blank = True, validators = [validate_mark])
    mg = models.BooleanField("Miễn giảm", default = False)
    tb = models.FloatField("Điểm trung bình", null = True, blank = True, validators = [validate_mark])
    note = models.TextField("Ghi chú", blank = True)
    
    sent_mark=models.CharField("Đánh dấu đã gửi tin nhắn",max_length=19,default="0000000000000000000")
    current=models.BooleanField("Thuộc lớp hiện tại", default=True )
    
    subject_id = models.ForeignKey(Subject, verbose_name = "Môn")
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh", null = True, blank = True)        
    term_id    = models.ForeignKey(Term, verbose_name = "Kì")
    
    class Meta:
        verbose_name = "Bảng điểm"
        verbose_name_plural = "Bảng điểm"

    
    def save(self, force_insert=False, force_update=False, using=None):
        new = self.id is None
        super(Mark, self).save( force_insert=force_insert, force_update=force_update, using=using)
        if new:
            MarkTime.objects.create( mark_id = self)
            #SentMark.objects.create( mark_id = self)    
     

    def __unicode__(self):
        return self.subject_id.name + " " + str(self.term_id.number) + self.student_id.first_name
    def length(self,x):
        print x
        return 2
    def convertToList(self):
        list=[]
        strss=self.diem.split('|')
        for i,strs in enumerate(strss):
            str=strs.split('*')
            length=len(str)
            aList=[]
            for s in str:
                aList.append(s)
            list.append((length,aList))
        return list

class MarkTime(models.Model):
    
    mieng_1 = models.DateTimeField("Thời gian cập nhật điểm miệng 1", null = True, blank = True)
    mieng_2 = models.DateTimeField("Thời gian cập nhật điểm miệng 2", null = True, blank = True)
    mieng_3 = models.DateTimeField("Thời gian cập nhật điểm miệng 3", null = True, blank = True)

    mieng_4 = models.DateTimeField("Thời gian cập nhật điểm miệng 4", null = True, blank = True)
    mieng_5 = models.DateTimeField("Thời gian cập nhật điểm miệng 5", null = True, blank = True)
    mlam_1 = models.DateTimeField("Thời gian cập nhật điểm 15' 1", null = True, blank = True)
    mlam_2 = models.DateTimeField("Thời gian cập nhật điểm 15' 2", null = True, blank = True)
    mlam_3 = models.DateTimeField("Thời gian cập nhật điểm 15' 3", null = True, blank = True)
    mlam_4 = models.DateTimeField("Thời gian cập nhật điểm 15' 4", null = True, blank = True)
    mlam_5 = models.DateTimeField("Thời gian cập nhật điểm 15' 5", null = True, blank = True)
    
    mot_tiet_1 = models.DateTimeField("Thời gian cập nhật điểm 1 tiết 1", null = True, blank = True)
    mot_tiet_2 = models.DateTimeField("Thời gian cập nhật điểm 1 tiết 2", null = True, blank = True)
    mot_tiet_3 = models.DateTimeField("Thời gian cập nhật điểm 1 tiết 3", null = True, blank = True)
    mot_tiet_4 = models.DateTimeField("Thời gian cập nhật điểm 1 tiết 4", null = True, blank = True)
    mot_tiet_5 = models.DateTimeField("Thời gian cập nhật điểm 1 tiết 5", null = True, blank = True)
    
    ck = models.DateTimeField("Thời gian cập nhật điểm thi cuối kì", null = True, blank = True)
    tb = models.DateTimeField("Thời gian cập nhật điểm trung bình", null = True, blank = True)
    mark_id = models.OneToOneField(Mark, verbose_name = "Điểm")
    
    class Meta:
        verbose_name = "Bảng thời gian cập nhật điểm"
        verbose_name_plural = "Bảng thời gian cập nhật điểm"

    def __unicode__(self):
        return self.mark_id.__unicode__()
class TKMon(models.Model):
    mg = models.BooleanField("Miễn giảm",default = False)
    tb_nam = models.FloatField("Trung bình năm", null = True, blank = True, validators = [validate_mark])
    time = models.DateTimeField("Thời gian cập nhật điểm tổng kết", null = True, blank = True)
    sent = models.BooleanField("Đã gửi ",default = False)
    #danh dau xem mon nay co dc phep thi lai hay ko
    thi_lai = models.BooleanField("Có thi lại", blank = True, default = False)
    diem_thi_lai=models.FloatField("Điểm thi lại", null = True, blank = True, validators = [validate_mark])
    # all fields can be null
    current=models.BooleanField("Thuộc lớp hiện tại", default=True )


    subject_id = models.ForeignKey(Subject, verbose_name = "Môn")
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    
    class Meta:
        verbose_name = "Trung bình môn"
        verbose_name_plural = "Trung bình môn"        
    #class Admin: pass
    def __unicode__(self):
        return self.subject_id.name + " " + self.student_id.first_name
    def timeToDigit(self):
        if not self.time:
            return ""
        else:
            return int((self.time-CHECKED_DATE).total_seconds()/60)
class KhenThuong(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh", null = True)
    term_id = models.ForeignKey(Term, verbose_name = "Kì", null = True)
    
    time = models.DateField("Thời gian(*)", blank = True)
    hinh_thuc = models.CharField("Hình thức(*)", max_length = 100, choices = KT_CHOICES)
    dia_diem= models.CharField("Địa điểm", max_length = 100, blank = True, null = True)
    noi_dung = models.CharField("Nội dung", max_length = 400, blank = True, null = True) # description
    luu_hoc_ba = models.BooleanField("Lưu học bạ", blank = True, default = False)
    
    class Meta:
        verbose_name = "Khen thưởng"
        verbose_name_plural = "Khen thưởng"
        
    def __unicode__(self):
        return self.hinh_thuc

class KiLuat(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    term_id = models.ForeignKey(Term, verbose_name = "Kì")
    
    time = models.DateField("Thời gian(*)", blank = True)
    hinh_thuc = models.CharField("Hình thức(*)", max_length = 35, choices = KL_CHOICES)
    dia_diem= models.CharField("Địa điểm", max_length = 100, blank = True, null = True)
    noi_dung = models.CharField("Nội dung", max_length = 400, blank = True, null = True) # description
    luu_hoc_ba = models.BooleanField("Lưu học bạ", blank = True, default = False)
    
    class Meta:
        verbose_name = "Kỉ luật"
        verbose_name_plural = "Kỉ luật"
        
    def __unicode__(self):
        return self.hinh_thuc
        
class HanhKiem(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    year_id = models.ForeignKey(Year, verbose_name = "Năm học")    
#    #danh dau ren luyen lai trong giai doan he
    ren_luyen_lai=models.NullBooleanField("Rèn luyện lại", blank = True, null = True)
    hk_ren_luyen_lai=models.CharField("Hạnh kiểm rèn luyện lại", null=True, blank=True, max_length = 2, choices = HK_CHOICES)
    class Meta:
        verbose_name = "Hạnh kiểm"
        verbose_name_plural = "Hạnh kiểm"
    
    def __unicode__(self):
        return unicode(self.student_id) + '-' + unicode(self.year_id)

        
class TBHocKy(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    term_id = models.ForeignKey(Term, verbose_name = "Kì")

    number_subject=models.SmallIntegerField("số lượng môn",null=True,blank=True, default=0)
    number_finish =models.SmallIntegerField("số lượng môn đã tổng kết xong", default=0)
    sent = models.BooleanField("Sent", default=False)

    tb_hk = models.FloatField("Trung bình học kì", validators = [validate_mark], null = True, blank = True)
    hl_hk = models.CharField("Học lực", max_length = 3, choices = HL_CHOICES, null = True, blank = True)
    danh_hieu_hk = models.CharField("Danh hiệu", max_length = 2, choices = DH_CHOICES, null = True, blank = True)
    
    class Meta:
        verbose_name = "Trung bình học kì"
        verbose_name_plural = "Trung bình học kì"
    
    def __unicode__(self):
        return  str(self.tb_hk) + " " + self.term_id.__unicode__() + self.student_id.__unicode__()
        
class TBNam(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    year_id = models.ForeignKey(Year, verbose_name = "Năm học")
    
    number_subject=models.SmallIntegerField("số lượng môn",null=True,blank=True, default=0)
    number_finish =models.SmallIntegerField("số lượng môn chưa tổng kết xong", default=0)
    
    tb_nam = models.FloatField("Trung bình năm", validators = [validate_mark], null = True, blank = True)
    hl_nam=models.CharField("Học lực", max_length = 3, choices = HL_CHOICES, null = True, blank = True)
    #hanh kiem nam
    term1 = models.CharField("Kì 1",max_length = 2, choices = HK_CHOICES, null=True,blank=True)
    term2 = models.CharField("Kì 2",max_length = 2, choices = HK_CHOICES, null=True,blank=True)
    year = models.CharField("Cả năm",max_length = 2, choices = HK_CHOICES, null=True,blank=True)
    #danh dau ren luyen lai trong giai doan he
    ren_luyen_lai=models.NullBooleanField("Rèn luyện lại", blank = True, null = True)
    hk_ren_luyen_lai=models.CharField("Hạnh kiểm rèn luyện lại", null=True, blank=True, max_length = 2, choices = HK_CHOICES)
    
    #hk_nam=models.CharField("Hạnh kiểm",max_length = 2, choices = HK_CHOICES, null = True, blank = True)
    tong_so_ngay_nghi=models.SmallIntegerField("Số ngày nghỉ", null = True, blank = True)
    #ghi danh hieu ma hoc sinh dat dc trong hoc ky    
    danh_hieu_nam=models.CharField("Danh hiệu", max_length = 2, choices = DH_CHOICES,null=True,blank=True)
    len_lop=models.NullBooleanField("Lên lớp", choices = LENLOP_CHOICES, null = True, blank = True)
    #danh dau thi lai
    
    thi_lai = models.NullBooleanField("Thi lại", null=True,blank=True)
    tb_thi_lai=models.FloatField("Trung bình thi lại", null = True, blank = True, validators = [validate_mark])
    hl_thi_lai=models.CharField("Học lực thi lại", null = True, blank=True, max_length = 3, choices = HL_CHOICES)
    sent = models.BooleanField("Sent", default=False)
    #len_lop_sau_he=models.NullBooleanField(null=True,blank = True,choices =LENLOP_CHOICES)

    class Meta:
        verbose_name = "Trung bình năm"
        verbose_name_plural = "Trung bình năm"
    def __unicode__(self):
        return self.student_id.__unicode__() + " " + str(self.year_id.__unicode__()) + " " + str(self.tb_nam)

    def convertHk(self, x):
        if x=='T':
            return u'Tốt'
        elif x=='K':
            return u'Khá'
        elif x=='TB':
            return u'TB'
        elif x=='Y':
            return u'Yếu'

    def get_hk_term1(self):
        if self.term1:
            return self.convertHk(self.term1)
        else:
            return "Chưa xét"
    
    def get_hk_term2(self):
        if self.term2:
            return self.convertHk(self.term2)
        else:
            return "Chưa xét"

    def get_hk_year(self):
        if self.year:
            return self.convertHk(self.year)
        else:
            return "Chưa xét"


class DiemDanh(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    term_id = models.ForeignKey(Term, verbose_name = "Kì")
    
    time = models.DateField("Ngày")
    loai = models.CharField("Tình trạng", max_length = 10, choices = DIEM_DANH_TYPE, default = 'k') 
    
    class Meta:
        verbose_name = "Điểm danh"
        verbose_name_plural = "Điểm danh"
        unique_together = ("student_id", "time", "term_id")
        
    def __unicode__(self):
        return self.student_id.__unicode__() + " " + str(self.time)
        
class TKDiemDanh(models.Model):
    student_id = models.ForeignKey(Pupil, verbose_name = "Học sinh")
    term_id = models.ForeignKey(Term, verbose_name = "Kì")
    
    tong_so = models.IntegerField("Số buổi nghỉ", blank = True, null = True)
    co_phep = models.IntegerField("Số buổi có phép", blank = True, null = True)
    khong_phep = models.IntegerField("Số buổi không phép", blank = True, null = True)
    
    class Meta:
        verbose_name = "Tổng kết điểm danh"
        verbose_name_plural = "Tổng kết điểm danh"

    def __unicode__(self):
        return self.student_id.__unicode__()

class TKB(models.Model):
    class_id = models.ForeignKey(Class, verbose_name= "Lớp")
    day = models.SmallIntegerField("Thứ", choices=DAY_CHOICE)
    period_1 = models.ForeignKey(Subject, related_name="Tiết 1", blank = True, null = True)
    period_2 = models.ForeignKey(Subject, related_name="Tiết 2", blank = True, null = True)
    period_3 = models.ForeignKey(Subject, related_name="Tiết 3", blank = True, null = True)
    period_4 = models.ForeignKey(Subject, related_name="Tiết 4", blank = True, null = True)
    period_5 = models.ForeignKey(Subject, related_name="Tiết 5", blank = True, null = True)
    period_6 = models.ForeignKey(Subject, related_name="Tiết 6", blank = True, null = True)
    period_7 = models.ForeignKey(Subject, related_name="Tiết 7", blank = True, null = True)
    period_8 = models.ForeignKey(Subject, related_name="Tiết 8", blank = True, null = True)
    period_9 = models.ForeignKey(Subject, related_name="Tiết 9", blank = True, null = True)
    period_10 = models.ForeignKey(Subject, related_name="Tiết 10", blank = True, null = True)
    chaoco = models.IntegerField("Tiết chào cơ", null= True)
    sinhhoat= models.IntegerField("Tiết sinh hoạt", null= True)

class Lesson(models.Model):
    subject_id = models.ForeignKey(Subject, verbose_name="Môn")
    index = models.IntegerField("Thứ tự", default = 0)
    title = models.TextField("Tên bài học", blank = True, null = True)
    note = models.TextField("Ghi chú", blank = True, null = True)
    ngay_day = models.DateField("Ngày dạy", blank = True, null = True)
    def __unicode__(self):
        return self.subject_id.__unicode__() + u' Tiết ' + str(self.index)
