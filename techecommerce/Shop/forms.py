#import form
from django import forms
#registration form
from django.contrib.auth.forms import UserCreationForm
#to store the details in DB
from django.contrib.auth.models import User
#for login and UsernameField: login by using username during registration
from django.contrib.auth.forms import AuthenticationForm, UsernameField
#standard translation related to password
from django.utils.translation import gettext, gettext_lazy as _

#Registration and form-control: bootstrap beautification
class CustomerRegistrationForm(UserCreationForm):

    #password
    #bootstrap class: {'class': 'form-control'}
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #confirm password
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    #to save data into DB 
    class Meta:
        #User table
        model = User
        #views on front end and DB fields
        fields = ['username', 'email', 'password1', 'password2']

        #modified labels
        labels = {'email': 'Email'}

        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

#user login and form-control: bootstrap beautification
class LoginForm(AuthenticationForm):
    username = UsernameField(widget= forms.TextInput(attrs= {'autofocus': True, 'class': 'form-control'}))
    #strip:False, keeps the password as it is. 
    password = forms.CharField(label = ('Password'), strip = False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))
