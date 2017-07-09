from django.shortcuts import render
from django.http import Http404

from book.models import Facility_master

# Create your views here.

def index(request):
    facility =Facility_master.objects.exclude(active='False')
    return render(request, 'book/index.html', {
        'facility': facility,
        })