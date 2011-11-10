from django.db import models
import helpers

# Create your models here.
class TrackImage(models.Model):
	shortcode=models.SlugField()
	image=models.ImageField(upload_to="Images/Uploads/%Y/%m/%d")
	keywords=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	description=models.TextField(blank=True, null=True)
	num_visits=models.IntegerField(default=0)
	date_created=models.DateTimeField()
	
	def save(self, **kwargs):
		slug_str=self.keywords
		helpers.unique_slugify(self, slug_str, slug_field_name='shortcode') 
		super(TrackImage, self).save()
		
class TrackImageVisit(models.Model):
	date_visited=models.DateTimeField()
	user_agent=models.TextField()
	ip=models.IPAddressField()
	image_tracked=models.ForeignKey(TrackImage)
	