from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Add, remove, change personal information
    (r'^$', 'help.views.help'),
    (r'^sitemap$', 'help.views.sitemap'),
    (r'^sitemapFrame$', 'help.views.sitemapFrame'),
    (r'^QLNT_Menu$', 'help.views.QLNT_Menu'),
    (r'^QLNT_Welcome$', 'help.views.QLNT_Welcome'),
    (r'^QLNT_LienheGopy$', 'help.views.QLNT_LienheGopy'),
    (r'^QLNT_Dangky$', 'help.views.QLNT_Dangky'),
    (r'^QLNT_Dangnhap$', 'help.views.QLNT_Dangnhap'),
    (r'^QLNT_QL$', 'help.views.QLNT_QL'),
    (r'^QLNT_QL_SuaTK$', 'help.views.QLNT_QL_SuaTK'),
    (r'^QLNT_QL_Thietlap$', 'help.views.QLNT_QL_Thietlap'),
    (r'^QLNT_QL_Thoikhoabieu$', 'help.views.QLNT_QL_Thoikhoabieu'),
    (r'^QLNT_QL_Chuyenlop$', 'help.views.QLNT_QL_Chuyenlop'),
    (r'^QLNT_QL_BaocaoTongket$', 'help.views.QLNT_QL_BaocaoTongket'),
    (r'^QLNT_QL_Giaovien$', 'help.views.QLNT_QL_Giaovien'),
    (r'^QLNT_QL_Lopvachunhiem$', 'help.views.QLNT_QL_Lopvachunhiem'),
    (r'^QLNT_QL_Lophoc$', 'help.views.QLNT_QL_Lophoc'),
    (r'^QLNT_QL_Diem$', 'help.views.QLNT_QL_Diem'),
    (r'^QLNT_QL_Hanhkiem$', 'help.views.QLNT_QL_Hanhkiem'),
    (r'^QLNT_QL_Sapxep$', 'help.views.QLNT_QL_Sapxep'),
    (r'^QLNT_QL_Diemdanh$', 'help.views.QLNT_QL_Diemdanh'),
    (r'^QLNT_QL_Lichhoc$', 'help.views.QLNT_QL_Lichhoc'),
    (r'^QLNT_QL_Tongket$', 'help.views.QLNT_QL_Tongket'),
    (r'^QLNT_QL_Xeploai$', 'help.views.QLNT_QL_Xeploai'),
    (r'^QLNT_QL_Monhoc$', 'help.views.QLNT_QL_Monhoc'),
    (r'^QLNT_QL_Nhantin$', 'help.views.QLNT_QL_Nhantin'),

    (r'^QLNT_GV$', 'help.views.QLNT_GV'),
    (r'^QLNT_GV_Xem$', 'help.views.QLNT_GV_Xem'),
    (r'^QLNT_GV_Danhsachloptoantruong$', 'help.views.QLNT_GV_Danhsachloptoantruong'),
    (r'^QLNT_GV_Giaovientoantruong$', 'help.views.QLNT_GV_Giaovientoantruong'),
    (r'^QLNT_GV_Quanlicaclop$', 'help.views.QLNT_GV_Quanlicaclop'),

    (r'^QLNT_HS$', 'help.views.QLNT_HS'),
    (r'^QLNT_HS_Lophoc$', 'help.views.QLNT_HS_Lophoc'),


    )
