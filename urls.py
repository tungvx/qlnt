from django.conf.urls.defaults import patterns, include, url
import settings 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name = "index"),
    # the built-in sign-in/out module 
    url(r'^login/$', 'app.views.login', name = "login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'app/logout.html'}, name = "logout"),
    url(r'^register/$', 'app.views.register', name = 'register'),
    url(r'^manageRegister/$', 'app.views.manage_register', name='manage_register'),
    url(r'^manageRegister/(?P<sort_by_date>\w+)/$', 'app.views.manage_register'),
    url(r'^manageRegister/(?P<sort_by_date>\w+)/(?P<sort_by_status>\w+)/$', 'app.views.manage_register'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # urls for app app
    url(r'^app/', include('app.urls')),
    
    # url for school app
    url(r'^school/', include('school.urls')),

    # url for reporting app
    url(r'^report/', include('reporting.urls')),
    
#    url(r'^sms/', include('sms.urls')),
#    url(r'^report', include('report.urls')),
#    (r'^topdf/$', 'views.topdf'),

    url(r'^profiles/', include('profiles.urls')),

    url(r'^profile/', 'views.get_absolute_url'),

    #url for help app
    url(r'^help/', include('help.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

    #urls for django-sentry
#    (r'^sentry/', include('sentry.web.urls')),
)
