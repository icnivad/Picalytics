from django.conf.urls.defaults import *
from django.views.generic import *
from views import *

urlpatterns=patterns('', 
	url(r'^$', create_image, name='create_image'),
	url(r'^list$', image_list, name='image_list'),
	url(r'^get/(?P<short_code>\w.*)/(?P<image_name>\w.*)', fetch_image, name='fetch_image'),
	url(r'^detail/(?P<short_code>\w.*)', image_detail, name='image_detail'),
)