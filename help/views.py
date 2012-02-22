#from report.models import ReceiverReportForm, SendReportForm
#from app.models import PositionTypeForm
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
#help.html extend base.html, include 2 iframe named: QLNT_Menu.html-MenuBar & QLNT_Welcome.html-contentHelp
def help(request):
    return render_to_response("help/help.html", context_instance=RequestContext(request))
#sitemap.html extend base.html, contain an iframe called sitemapFrame.html
def sitemap(request):
    return render_to_response("help/sitemap.html", context_instance=RequestContext(request))
def sitemapFrame(request):
    return render_to_response("help/sitemapFrame.html", context_instance=RequestContext(request))
def QLNT_Menu(request):
    return render_to_response("help/QLNT_Menu.html", context_instance=RequestContext(request))
def QLNT_Welcome(request):
    return render_to_response("help/QLNT_Welcome.htm", context_instance=RequestContext(request))
def QLNT_Dangky(request):
    return render_to_response("help/QLNT_Dangky.html", context_instance=RequestContext(request))
def QLNT_Dangnhap(request):
    return render_to_response("help/QLNT_Dangnhap.html", context_instance=RequestContext(request))
def QLNT_LienheGopy(request):
    return render_to_response("help/QLNT_LienheGopy.html", context_instance=RequestContext(request))
def QLNT_QL(request):
    return render_to_response("help/QLNT_QL.html", context_instance=RequestContext(request))
def QLNT_QL_SuaTK(request):
    return render_to_response("help/QLNT_QL_SuaTK.html", context_instance=RequestContext(request))
def QLNT_QL_Thietlap(request):
    return render_to_response("help/QLNT_QL_Thietlap.html", context_instance=RequestContext(request))
def QLNT_QL_Thoikhoabieu(request):
    return render_to_response("help/QLNT_QL_Thoikhoabieu.html", context_instance=RequestContext(request))
def QLNT_QL_Chuyenlop(request):
    return render_to_response("help/QLNT_QL_Chuyenlop.html", context_instance=RequestContext(request))
def QLNT_QL_BaocaoTongket(request):
    return render_to_response("help/QLNT_QL_BaocaoTongket.html", context_instance=RequestContext(request))
def QLNT_QL_Giaovien(request):
    return render_to_response("help/QLNT_QL_Giaovien.html", context_instance=RequestContext(request))
def QLNT_QL_Lopvachunhiem(request):
    return render_to_response("help/QLNT_QL_Lopvachunhiem.html", context_instance=RequestContext(request))
def QLNT_QL_Lophoc(request):
    return render_to_response("help/QLNT_QL_Lophoc.html", context_instance=RequestContext(request))
def QLNT_QL_Diemdanh(request):
    return render_to_response("help/QLNT_QL_Diemdanh.html", context_instance=RequestContext(request))
def QLNT_QL_Lichhoc(request):
    return render_to_response("help/QLNT_QL_Lichhoc.html", context_instance=RequestContext(request))
def QLNT_QL_Diem(request):
    return render_to_response("help/QLNT_QL_Diem.html", context_instance=RequestContext(request))
def QLNT_QL_Hanhkiem(request):
    return render_to_response("help/QLNT_QL_Hanhkiem.html", context_instance=RequestContext(request))
def QLNT_QL_Sapxep(request):
    return render_to_response("help/QLNT_QL_Sapxep.html", context_instance=RequestContext(request))
def QLNT_QL_Tongket(request):
    return render_to_response("help/QLNT_QL_Tongket.html", context_instance=RequestContext(request))
def QLNT_QL_Monhoc(request):
    return render_to_response("help/QLNT_QL_Monhoc.html", context_instance=RequestContext(request))
def QLNT_QL_Nhantin(request):
    return render_to_response("help/QLNT_QL_Nhantin.html", context_instance=RequestContext(request))
def QLNT_QL_Xeploai(request):
    return render_to_response("help/QLNT_QL_Xeploai.html", context_instance=RequestContext(request))


def QLNT_GV_Xem(request):
    return render_to_response("help/QLNT_GV_Xem.html", context_instance=RequestContext(request))
def QLNT_GV_Danhsachloptoantruong(request):
    return render_to_response("help/QLNT_GV_Danhsachloptoantruong.html", context_instance=RequestContext(request))
def QLNT_GV_Giaovientoantruong(request):
    return render_to_response("help/QLNT_GV_Giaovientoantruong.html", context_instance=RequestContext(request))
def QLNT_GV_Quanlicaclop(request):
    return render_to_response("help/QLNT_GV_Quanlicaclop.html", context_instance=RequestContext(request))
def QLNT_GV(request):
    return render_to_response("help/QLNT_GV.html", context_instance=RequestContext(request))

def QLNT_HS(request):
    return render_to_response("help/QLNT_HS.html", context_instance=RequestContext(request))
def QLNT_HS_Lophoc(request):
    return render_to_response("help/QLNT_HS_Lophoc.html", context_instance=RequestContext(request))
