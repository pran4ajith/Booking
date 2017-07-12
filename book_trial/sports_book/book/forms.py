from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import (
    authenticate, 
    login, 
    get_user_model,
    logout,
    )

User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={ 'placeholder':'Enter your username',}

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
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("This user isn't active")

        return super(UserLoginForm, self).clean(*args, **kwargs)
        
class UserRegisterForm(forms.ModelForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter you email address',}

        ), label='Email address')
    username = forms.CharField(widget=forms.TextInput(
        attrs={ 'placeholder':'Enter your username',}

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
        fields = [ 'username', 'email', 'password', 'password2']

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
