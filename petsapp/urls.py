from django.urls import path
from .import views
urlpatterns=[
    path('pets_list/',views.pets_list,name='pets_list'),
    path('pet_detail/<int:pk>',views.pet_detail,name='pet_detail'),
    path('dog-list/',views.dog_list,name='dog-list'),
    path('cat-list/',views.cat_list,name='cat-list'),
    path('search/',views.search,name='search')
]