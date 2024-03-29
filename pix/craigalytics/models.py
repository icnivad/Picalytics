from django.db import models
import helpers

# the keyword field is used to generate the shortcode
# used to track ads.  
class TrackImage(models.Model):
	shortcode=models.SlugField()
	image=models.ImageField(upload_to="Images/Uploads/%Y/%m/%d")
	keywords=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	description=models.TextField(blank=True, null=True)
	num_visits=models.IntegerField(default=0)
	date_created=models.DateTimeField()
	
	# converts keyword field into shortcode
	# the method unique_slugify adds a unique id to the end to ensure uniqueness
	def save(self, **kwargs):
		slug_str=self.keywords
		helpers.unique_slugify(self, slug_str, slug_field_name='shortcode') 
		super(TrackImage, self).save()
		
# At some point, I would like to introduce a plugin to convert ip address
# to a location predictor
class TrackImageVisit(models.Model):
	date_visited=models.DateTimeField()
	user_agent=models.TextField()
	ip=models.IPAddressField()
	image_tracked=models.ForeignKey(TrackImage)
	