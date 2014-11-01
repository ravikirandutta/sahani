from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from notifications import notify
import os

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos','users', str(instance.id), filename)

class ChefProfile(models.Model):

	user = models.OneToOneField(User)
	about_me = models.TextField()
	food_philosophy = models.TextField()
	mobile_no = models.CharField(max_length=15)
	#blog_url = models.URLField(default='')
	profile_image = models.FileField(upload_to=get_image_path, blank=True, null=True)

	def __unicode__(self):
    		return smart_unicode(self.user)

class ChefDish(models.Model):

	chef = models.ForeignKey(ChefProfile)
	dish_name  = models.CharField(max_length=400)
	dish_description = models.TextField()
	dish_photo = models.CharField(max_length=400)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')



# class ThaliProfile(models.Model)

# 	user = models.OneToOneField(User)
# 	about_me = models.TextField()
# 	food_philosophy = models.TextField()
# 	mobile_no = models.charField()
# 	blog_url = models.URLField(default='')


# 	def __unicode__(self):
#         return smart_unicode(self.user)