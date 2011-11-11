from django.conf.urls.defaults import patterns, include, url
import settings, suburls

urlpatterns = patterns('',
    (r'^%s' % settings.SUBSITE , include(suburls))
)
