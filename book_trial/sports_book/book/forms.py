#THIS IS WHERE FORMS ARE DEFINED AND ARE CALLED FROM VIEWS.

from django.contrib.auth.models import User
from django import forms
from models import Facility_master, Facility_availability, Book_Facility
from django.contrib.auth import (
	authenticate,
	login,
	get_user_model,
	logout,
	)
from django.contrib.auth.forms import UserChangeForm
import datetime
from django.forms.extras.widgets import SelectDateWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

User = get_user_model()
# user login form
class UserLoginForm(forms.Form):
	username = forms.CharField(label='Employee id', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your Employee ID',}

		))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={ 'placeholder':'Enter your password',}

		))
	def clean(self, *args, **kwargs):#dont know why args and kwargs
		username= self.cleaned_data.get("username")
		password= self.cleaned_data.get("password")
		'''user_qs = User.objects.filter(username=username)
		if user_qs.count() == 1:
			user= user_qs.first()'''
		if username and password:
			user= authenticate(username= username, password=password)
			if not user:
				raise forms.ValidationError("Please enter a valid username or password")

			if not user.is_active:
				raise forms.ValidationError("This user isn't active")

		return super(UserLoginForm, self).clean(*args, **kwargs)


#facility booking form
class FacilityBookForm(forms.ModelForm):

	class Meta:
		model = Book_Facility
		fields= ['facility', 'event', 'book_date', 'time_start', 'time_end',]
		widgets = {
            #Use localization and bootstrap 3
            'book_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'time_start': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
            'time_end': TimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
        }

	def clean_book_date(self):
		book_date = self.cleaned_data['book_date']#to check if date is in past
		if book_date < datetime.date.today():
			raise forms.ValidationError("The date cannot be in the past!")
		return book_date


		time_start=forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))#widget inside this is not necessary
        time_end=forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))


#user registration form
class UserRegisterForm(forms.ModelForm):#a modelform based on user model
	email= forms.EmailField(widget=forms.EmailInput(attrs={
		'placeholder': 'Enter you email address',}

		), label='Email address')
	username = forms.CharField(label='Employee id', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your Employee id',}

		))
	first_name= forms.CharField(label='First Name', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your First Name',}

		))
	last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your Last Name',}

		))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={ 'placeholder':'Enter your password',}

		))
	password2= forms.CharField(label= 'Confirm Password',
		widget=forms.PasswordInput(
		attrs={ 'placeholder':'Confirm your password',}

		))
	class Meta:
		model = User
		fields = [ 'username', 'email','first_name','last_name', 'password', 'password2',]

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		return first_name
	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		return last_name
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs= User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email already registered")
		return email
	def clean_password2(self):
		password = self.cleaned_data.get('password')
		if len(password) < 8:
			raise forms.ValidationError('Password too short. Password should have minimum 8 characters.')
		password2 = self.cleaned_data.get('password2')

		if password != password2:
			raise forms.ValidationError("The passwords do not match")
		return password

class EditProfileForm(forms.ModelForm):#modelform based on user model
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	username = forms.CharField(label='Employee id', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your Employee id',}
		))

	class Meta:
		model = User
		fields = ['username','email', 'first_name', 'last_name']
	def clean_username(self):
		username = self.cleaned_data.get('username')
		return username
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs= User.objects.filter(email=email).exclude(pk=self.instance.pk)#to disable checking the logged in user
		if email_qs.exists():
			raise forms.ValidationError("Email already registered")
		return email
	def save(self, commit=True):
		user_edit = super(EditProfileForm, self).save(commit=False)
		if commit:
			user_edit.save()
		return user_edit



