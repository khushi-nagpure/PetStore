from django.shortcuts import render,HttpResponse
from .models import pet
from django.http import Http404
from django.db.models import Q

# Create your views here.

def pets_list(request):
    pets_data = pet.objects.all()
    data = {'pets_d':pets_data}
    return render(request,'petsapp/list.html',data)

def pet_detail(request,pk):
    query = pet.objects.filter(id=pk)
    if query.exists() and query.count()==1:
        instance = query.first()
    else:
        return Http404("Pet data does not Exists")
    context = {
        'data':instance
    }
    return render(request,'petsapp/detail.html',context)

def dog_list(request):
    dog_data = pet.objects.filter(animal_type="D")
    all_dog_data ={
        'objects':dog_data
    }
    return render(request,'petsapp/dog-list.html',all_dog_data)

def cat_list(request):
    cat_data = pet.objects.filter(animal_type="C")
    all_cat_data ={
        'objectsc':cat_data
    }
    return render(request,'petsapp/cat-list.html',all_cat_data)

def search(request):
    if request.method =="GET":
        searched_data = request.GET.get('search')
        if(len(searched_data)==0):
            return Http404("No Such Data")
        else:
            #result = pet.objects.filter(name__icontains=searched_data)
            query = (Q(name__icontains=searched_data) | Q(breed__icontains=searched_data)
                     | Q(species__icontains=searched_data) | Q(description__icontains=searched_data))
            result = pet.objects.filter(query)
            
            context = {
                'object':result
            }
            return render ( request,'petsapp/search.html',context)
    else:
        return HttpResponse("Invalid Method")


    
    
    
    
    
