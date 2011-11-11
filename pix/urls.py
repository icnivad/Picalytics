from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import suburls

urlpatterns = patterns('',
    (r'^%s' % settings.SUBSITE , include(suburls))
)
