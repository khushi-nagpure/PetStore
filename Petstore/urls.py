"""
URL configuration for Petstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from account.views import register,MyLoginView,MyLogoutView
#from django.contrib.auth import views as auth_view
from petsapp.views import pets_list
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pets_list,name='home'),
    path('petsapp/',include('petsapp.urls'),name='pets'),
    path('cart/',include('cart.urls'),name='cart'),
    path('orders/',include('orders.urls'),name='orders'),
    path('register/',register,name='register-page'),
    path('login/',MyLoginView.as_view(template_name='base/login.html'),name='login'),
    path('logout/',MyLogoutView.as_view(),name='logout'),
    path('orders_history/',views.orders_history,name='orders_history'),
]

if settings:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
