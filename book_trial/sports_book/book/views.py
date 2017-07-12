from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import Http404

from book.models import Facility_master
from django.contrib.auth import (
    authenticate, 
    login, 
    get_user_model,
    logout,
    )
from django.contrib.auth.decorators import login_required
#add @login_required(login_url='/login/')
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.

#home
def index(request):
    facilities =Facility_master.objects.exclude(active='False')
    return render(request, 'book/index.html', {
        'facilities': facilities,
        })
#facility booking
def facility_detail(request, id):
    try:
        facility= Facility_master.objects.get(id=id)
    except Facility_master.DoesNotExist:
        raise Http404('The facility is not available')
    return render(request, 'book/facility_detail.html', {
        'facility':facility,
        })

#login
def login_view(request):
    print request.user.is_authenticated()
    title= "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        #redirect
        return redirect("/")
    return render(request, "book/login_form.html", {"form":form, "title":title})


#register
def register_view(request):
    print request.user.is_authenticated()
    title= "Register"
    form= UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username= user.username, password=password)
        login(request, new_user)
        return redirect("/")
        #return

    return render(request, "book/register_form.html", {"form":form, "title":title})


#logout
def logout_view(request):
    logout(request)
    return redirect("/")