from django.shortcuts import render,redirect  
from .forms import RegistrationForm 
from django.contrib import messages
from petsapp.views import pets_list
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy


# Create your views here.

def register(request):
    if request.method =="GET":
        form = RegistrationForm()
        return render(request,'base/register.html',{'form_data':form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request,'Account created Successfully For'+'  '+ user_name)
            return redirect('pets_list')
        else:
            messages.error(request,'OOPS something went wrong please try again')
            return render(request,'base/register.html',{'form_data':form})
        
    return render(request,'base/register.html',{'form_data':form})

class MyLoginView(LoginView):
    def form_valid(self,form):
        messages.success(self.request,'Login sucessfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Invalid username or password')
        return super().form_invalid(form)
    
class MyLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request,'Logout successfully')
        return reverse_lazy('home')