from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import password_change, password_change_done

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^accounts/login/$', 'gramy.views.login_view'),
                       url(r'^logout/$', 'gramy.views.logout_view'),
                       url(r'^siata/', include('gramy.urls')),
                       url(r'^$', include('gramy.urls')),
                       url(r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
                       url(r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),

                       # Uncomment the admin/doc line below to enable admin documentation:
                           (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       # Uncomment the next line to enable the admin:
                           (r'^admin/', include(admin.site.urls)),
                       )



# if settings.DEBUG:
#     urlpatterns += patterns("django.views",
#                             url(r"^static/(?P<path>.*)", 
#                                 "static.serve", 
#                                 { "document_root": settings.MEDIA_ROOT,
#                                   'show_indexes': True })   
#                             )
