from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class Admin_setup(models.Model):
	name = models.CharField(max_length=200)
	emp_id = models.CharField(max_length=200)
	class Meta:
		verbose_name= 'Admin Setup'
		verbose_name_plural='Admin Setup'
	
'''
class Facility_master(models.Model):
	fac_id = models.CharField(max_length=200, verbose_name="ID")
	fac_name = models.CharField(max_length=200, verbose_name="Facility")#verbose_name for custom field name
	active = models.BooleanField(verbose_name="Active")
	description = models.TextField(verbose_name="Description")
	image = models.FileField(blank = True, verbose_name="Image")
	@property
	def getImage(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
	class Meta:
		verbose_name= 'Add Facility'
		verbose_name_plural='Add Facility'
	def __unicode__(self):
		return str(self.fac_name)

	'''
	In settings.py add the following for file upload

	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	MEDIA_URL = '/media/'
	'''


class Facility_availability(models.Model):
	fac_name = models.ForeignKey("Facility_master")
	#fac_id= models.
	day = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Day")
	start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Start Time")
	end_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="End Time")
	available= models.BooleanField(verbose_name="Available:", default= True)
	class Meta:
		verbose_name= 'Facility Availability'
		verbose_name_plural='Facility Availability'


class Book_Facility(models.Model):
	username = models.ForeignKey(User)
	event = models.CharField(max_length=20, verbose_name="Event", blank=True)
	#fac_name = models.OneToOneField(Facility_master,on_delete=models.CASCADE,primary_key=True)
	#fac_name = models.ForeignKey("Facility_master")
	facility=models.ForeignKey("Facility_master")
	book_date= models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date")
	time_start= models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Start Time")
	time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="End Time")
	class Meta:
		verbose_name= 'User Booking'
		verbose_name_plural='User Bookings'

	

















'''class user(models.Model):
	user= models.ForeignKey('auth.User', verbose_name="USER", blank=True, null=True)
	first_name= models.CharField(verbose_name="First Name", max_length=30)
	last_name= models.CharField(verbose_name="First Name", max_length=30)
	emp_id= models.CharField(verbose_name="Employee Number", max_length=300)
	email= models.EmailField(verbose_name="Email ID")
	phone= models.CharField(verbose_name="Phone Number", blank=True)
	class Meta:
		verbose_name= 'Facility Availability'
		verbose_name_plural='Facility Availability'
	def __unicode__(self):
		return str(self.user, self.emp_id)

class booking(models.Model):
	user_name= models.ForeignKey("user")
	date_from= models.DateTimeField(verbose_name="From")
	date_until=models.DateTimeField(verbose_name="Till")
'''