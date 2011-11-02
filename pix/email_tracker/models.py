from django.db import models

# Create your models here.
class TrackEmail(models.Model):
	email_to=models.EmailField()
	subject=models.CharField(max_length=200)
	body=models.TextField()
	shortcode=models.SlugField()

	def generate_shortcode(self):
		self.shortcode=""

class TrackLink(models.Model):
	link=models.URLField()
	tracked_email=models.ForeignKey(TrackEmail)
	click_count=models.IntegerField(default=0)
