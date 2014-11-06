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


class DishReview(models.Model):

	chef = models.ForeignKey(ChefProfile)
	dish  = models.ForeignKey(ChefDish)
	review = models.TextField()
	reviewer = models.OneToOneField(User)

class Address(models.Model):

	user = models.OneToOneField(User)

	address_line1 = models.CharField(max_length=1000)
	address_line2 = models.CharField(max_length=1000)
	City = models.CharField(max_length=1000)
	zipcode = models.CharField(max_length=1000)
	state = models.CharField(max_length=1000)
	country = models.CharField(max_length=1000)
	extra_instructions = models.TextField()

class Rating(models.Model):

    dish = models.ForeignKey(ChefDish)
    chef = models.ForeignKey(ChefProfile)
    rater = models.ForeignKey(User)

    rating_value = models.FloatField(default=0)
    already_rated = models.BooleanField(default=False) # If already rated then nothing can be changed.

    def __unicode__(self):
        return smart_unicode(self.rating_value)

    def set_rating(self,value):
        if self.already_rated :
            pass# do nothing as user is trying to double vote

        else :
            rating_value = value

