from django.conf.urls.defaults import *

urlpatterns = patterns('gramy.views',
                       (r'^gramy/szczegoly/(?P<id>.+)/$', 'szczegoly'),
                       (r'^gramy/$', 'lista'),
                       (r'^$', 'lista')
                       )
