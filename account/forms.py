from django import forms 
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2','check']
    
    username = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}
        )
    )
    
    email = forms.EmailField(
        max_length= 100,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}
        )
    )
    
    first_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}
        )
    )
    
    last_name = forms.CharField(
        max_length= 100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}
        )
    )
    
    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your password','type':'password'}
    )
    
    )
    
    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':' confirm Your password','type':'password'}
    )
    
    )
    
    check = forms.BooleanField(required=True)
        
