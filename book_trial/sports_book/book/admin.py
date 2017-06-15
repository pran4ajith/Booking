from django.contrib import admin

# Register your models here.
from .models import Admin_setup, Facility_master, Facility_availability

admin.site.register(Admin_setup)
admin.site.register(Facility_master)
admin.site.register(Facility_availability)


