from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Admin_setup(models.Model):
	name = models.CharField(max_length=200)
	emp_id = models.CharField(max_length=200)


class Facility_master(models.Model):
	fac_id = models.CharField(max_length=200)
	fac_name = models.CharField(max_length=200)
	active = models.BooleanField()
	description = models.TextField()
	image = models.FileField(blank = True)
	'''
	In settings.py add the following for file upload

	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	MEDIA_URL = '/media/'
	'''


class Facility_availability(models.Model):
	def __unicode__(self):
		return unicode(self.fac_name)
	fac_name = models.OneToOneField('Facility_master', on_delete=models.CASCADE)
	day = models.CharField(max_length=20)
	start_time = models.TimeField(auto_now=False, auto_now_add=False)
	end_time = models.TimeField(auto_now=False, auto_now_add=False)