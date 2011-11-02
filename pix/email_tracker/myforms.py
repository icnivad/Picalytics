from django import forms
from django.forms import ModelForm
from models import TrackEmail

class TrackEmailForm(ModelForm):
	class Meta:
		model=TrackEmail
		exclude=('shortcode',)
