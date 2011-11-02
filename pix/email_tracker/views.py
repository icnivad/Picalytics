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
from models import  *
from django.conf import settings
import myforms

def send_email(request):
	email_form=myforms.TrackEmailForm()
	if request.method=="POST":
		email_form=myforms.TrackEmailForm(request.POST)
		email=email_form.save(commit=False)
		email.generate_shortcode()
		email.save()
		send_mail(email.subject, email.body, email.email_to, ['bearle2009@gmail.com'])
		c={'form':email_form}
		return render(request, 'email_sent.html', c)
	c={'form':email_form}
	return render(request, 'email_form.html', c)

def tracked_link(shortcode=""):
	pass
