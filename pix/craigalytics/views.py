# Create your views here.
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Context, Template, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
import simplejson
from django.template import RequestContext
import models
from django.conf import settings
import myforms


def create_image(request):
	form=myforms.TrackImageForm()
	if request.method=="POST":
		form=myforms.TrackImageForm(request.POST, request.FILES)
		img=form.save(commit=False)
		img.save()
		c={'form':form}
		return redirect(reverse('image_details'))
	c={'form':form}
	return render(request, 'image_create.html', c)

def fetch_image(request, short_code):
	image=models.TrackImage.objects.get(short_code=short_code)
	return render(request, 'fetch_image.html', {'image':image})
	
def image_detail(request, short_code):
	pass