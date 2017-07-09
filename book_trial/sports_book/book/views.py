from django.shortcuts import render
from django.http import Http404

from book.models import Facility_master

# Create your views here.

def index(request):
    facilities =Facility_master.objects.exclude(active='False')
    return render(request, 'book/index.html', {
        'facilities': facilities,
        })

def facility_detail(request, id):
    try:
        facility= Facility_master.objects.get(id=id)
    except Facility_master.DoesNotExist:
        raise Http404('The facility is not available')
    return render(request, 'book/facility_detail.html', {
        'facility':facility,
        })