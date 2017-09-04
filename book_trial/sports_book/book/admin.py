from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import Group #imported to remove -_-


# Register your models here.
from .models import  Facility_master, Facility_availability, Book_Facility

    
class Facility_masterAdmin(admin.ModelAdmin):
    list_display=['fac_id', 'fac_name', 'active'] #changing the dislayed colun name of tables django admin
class Facility_availabilityAdmin(admin.ModelAdmin):
    list_display=['fac_name', 'day', 'start_time', 'end_time', 'available']
class Book_FacilityAdmin(admin.ModelAdmin):
    list_display=['username', 'facility', 'event', 'book_date', 'time_start', 'time_end']

def my_function(self, fac_name):
    """My Custom Title"""
    my_function.short_description = 'proper' # :(


#admin.site.register(Admin_setup, Admin_setupAdmin)
admin.site.register(Facility_master, Facility_masterAdmin)
admin.site.register(Facility_availability, Facility_availabilityAdmin)
admin.site.register(Book_Facility, Book_FacilityAdmin)
admin.site.unregister(Group) #remove groups under users from admin page

''' Other changes to django admin are made by editing the root template and also have used django admin bootstrapped '''