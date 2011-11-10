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
import datetime

def create_image(request):
	form=myforms.TrackImageForm()
	if request.method=="POST":
		form=myforms.TrackImageForm(request.POST, request.FILES)
		img=form.save(commit=False)
		img.date_created=datetime.datetime.now()
		img.save()
		return redirect(reverse('image_detail', kwargs={'short_code':img.shortcode}))
	c={'form':form}
	return render(request, 'image_create.html', c)

def fetch_image(request, short_code, image_name):
	fetched=models.TrackImage.objects.get(shortcode=short_code)
	fetched.num_visits+=1
	fetched.save()
	track_visit=models.TrackImageVisit(image_tracked=fetched)
	track_visit.date_visited=datetime.datetime.now()
	track_visit.user_agent=request.META['HTTP_USER_AGENT']
	track_visit.ip=request.META['REMOTE_HOST']
	track_visit.save()
	return redirect(fetched.image.url)
	
def image_detail(request, short_code):
	image=models.TrackImage.objects.get(shortcode=short_code)	
	url=request.build_absolute_uri(reverse('fetch_image', kwargs={'short_code':image.shortcode, 'image_name':image.image.name.split("/")[-1]}))
	return render(request, 'image_detail.html', {'image':image, 'url':url})
	
def image_list(request):
	images=models.TrackImage.objects.all()
	return render(request, 'image_list.html', {'images':images})