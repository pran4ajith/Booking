from __future__ import unicode_literals
from django.contrib import admin


# Register your models here.
from .models import  Facility_master, Facility_availability

'''class Admin_setupAdmin(admin.ModelAdmin):
    list_display=['name', 'emp_id']'''
    
class Facility_masterAdmin(admin.ModelAdmin):
    list_display=['fac_id', 'fac_name', 'active']
class Facility_availabilityAdmin(admin.ModelAdmin):
    list_display=['fac_name', 'day', 'start_time', 'end_time']

def my_function(self, fac_name):
    """My Custom Title"""
    my_function.short_description = 'proper'


#admin.site.register(Admin_setup, Admin_setupAdmin)
admin.site.register(Facility_master, Facility_masterAdmin)
admin.site.register(Facility_availability, Facility_availabilityAdmin)


