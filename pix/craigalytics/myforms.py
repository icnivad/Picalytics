from django import forms
from django.forms import ModelForm
from models import TrackImage

class TrackImageForm(ModelForm):
	class Meta:
		model=TrackImage
		exclude=('shortcode','num_visits')
