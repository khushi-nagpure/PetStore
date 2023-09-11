from .models import Orders,Payment,OrderPet,pet
from django import forms
from django.forms import ModelForm

class OrderForm(forms.ModelForm):
    states = [
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('AS','Assam'),
        ('BR','Bihar'),
        ('GOA','Goa'),
        ('GJ','Gujrat'),
        ('RJ','Rajashtan'),
        ('MH','Maharashtra'),
        ('UP','Uttar Pradesh')]
    
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(widget=forms.Select(choices=states,attrs={'class':'form-control'}))
    country = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    class Meta :
        model = Orders
        fields = ['first_name','last_name','phone','email','address','country','state','city']