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

#Creates the image, uploading the image file to a subdirectory of Media/Images/Uploads
#the shortcode will be used to generate a url which is tracked, to inform the application
#of how often the image is viewed

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

# Fetches the image corresponding to the shortcode url
# Then records the user agent, ip address, date of visit, and updates the number of visits
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

# displays details about the image, including the number of visits, and detailed info on each visit
# also provides the <img> tag which should be copied into ads that are being tracked.
def image_detail(request, short_code):
	image=models.TrackImage.objects.get(shortcode=short_code)	
	visits=models.TrackImageVisit.objects.filter(image_tracked=image)
	url=request.build_absolute_uri(reverse('fetch_image', kwargs={'short_code':image.shortcode, 'image_name':image.image.name.split("/")[-1]}))
	return render(request, 'image_detail.html', {'image':image, 'url':url, 'visits':visits})
	
def image_list(request):
	images=models.TrackImage.objects.all()
	return render(request, 'image_list.html', {'images':images})