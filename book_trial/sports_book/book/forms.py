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

User = get_user_model()
# user login form
class UserLoginForm(forms.Form):
	username = forms.CharField(label='Employee id', widget=forms.TextInput(
		attrs={ 'placeholder':'Enter your Employee ID',}

		))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={ 'placeholder':'Enter your password',}

		))
	def clean(self, *args, **kwargs):
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
		fields= ['username','email', 'facility', 'event', 'book_date', 'time_start', 'time_end',]

'''    def __init__(self, *args, **kwargs):
		self.username = kwargs.pop('username')
		super(FacilityBookForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		inst = super(FacilityBookForm, self).save(commit=False)
		inst.author = self.username
		if commit:
			inst.save()
			self.save_m2m()
		return inst'''


#user registration form    
class UserRegisterForm(forms.ModelForm):
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
#forgot password
#class PasswordResetRequestForm(forms.Form):
	#email_or_username = forms.Charfield(label=("Email or Employee ID"),max_length=254)
#edit profile
'''class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = [
			
			'email',
			'first_name',
			'last_name',
			'password',

		]
	
'''

class EditProfileForm(forms.ModelForm):
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



''' def clean_email(self):
		email = self.cleaned_data.get('email')

		if email and User.objects.filter(email=email):
			raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
		return email'''

	
''' 	if commit:
			user.save()

		return user'''