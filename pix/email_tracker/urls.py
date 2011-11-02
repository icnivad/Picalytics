from django.conf.urls.defaults import *
from django.views.generic import *
from views import *

#today we're playing with generic views
urlpatterns = patterns('',
    url(r'^$', send_email, name='send_email'),
)
