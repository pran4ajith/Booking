from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.views.generic import UpdateView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from book.models import Facility_master, Book_Facility
from django.contrib.auth import (
    authenticate, 
    login, 
    get_user_model,
    logout,
    )
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
#add @login_required(login_url='/login/')
from .forms import UserLoginForm, UserRegisterForm, FacilityBookForm#, EditProfileForm
# Create your views here.

#home
def index(request):
    facilities =Facility_master.objects.exclude(active='False')
    return render(request, 'book/index.html', {
        'facilities': facilities,
        })
#facility display
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
        '''if user is not None and user.is_active and user.is_staff:      
            return redirect("/admin/")
        #redirect
        else:'''
        return redirect("/")
    return render(request, "login_reg/login_form.html", {"form":form, "title":title})


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

    return render(request, "login_reg/register_form.html", {"form":form, "title":title})


#logout
def logout_view(request):
    logout(request)
    return redirect("/")
#facilility booking
@login_required(login_url='/login/')
def booking_view(request): 
    form= FacilityBookForm(request.POST , instance=request.user)
    form.actual_user = request.user
    if form.is_valid():
        
        
        event = form.cleaned_data.get('event')
        book_date = form.cleaned_data.get('book_date')
        time_start = form.cleaned_data.get('time_start')
        time_end = form.cleaned_data.get('time_end')
        form.save()
        return redirect("/")
    return render(request, "book/book_form.html", {"form":form})


#edit details

'''undo for last
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('/editprofile/')

    else:
        form = EditProfileForm(instance= request.user)
        return render(request, "login_reg/edit_profile.html", {'form': form})
'''
'''
class edit_profile(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "login_reg/edit_profile.html"

    def get_object(self,request, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.user
    def get_success_url(self, *args, **kwargs):
        return reverse('/')
'''

@login_required(login_url='/login/')
def edit_profile(request):
    try:
        username = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return redirect('/')
    form= list()
    if request.method=='POST':
        username=request.POST['username']
        form=User.objects.get(username=username,)
        
        form.save()
        


        return render(request,"login_reg/edit_profile.html",{'form':form})
    else:
        return render(request,"login_reg/edit_profile.html",{'form':form})

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user ,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect("/changepassword/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user =request.user)
           
    return render(request, "book/change_password.html",{"form":form})
'''
def facility_detail(request, id):
    try:
        facility= Facility_master.objects.get(id=id)
    except Facility_master.DoesNotExist:
        raise Http404('The facility is not available')
    return render(request, 'book/facility_detail.html', {
        'facility':facility,
        })
'''
