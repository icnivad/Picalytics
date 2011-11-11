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
import datetime

def main(request):
	return render(request, 'main.html', {})