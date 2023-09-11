from django.shortcuts import render,redirect
from petsapp.models import pet
from .models import Cart
from django.contrib import messages
from django.db.models import F ,Sum
from django.http import JsonResponse
# Create your views here.

def add_to_cart(request,id):
    cart_id = request.session.session_key
    if cart_id == None:
        cart_id = request.session.create()
        
        
    Pet = pet.objects.get(id=id)
    price = Pet.price
    user = request.user
    if Cart.objects.filter(user=user, pet=Pet).exists() :
        messages.error(request,"Item already exist in the Cart")
    else:
    
        Cart(cart_id=cart_id,pet=Pet,user=user,totalprice=price).save()
        messages.success(request,"Item Added to Cart Successfully")
    return redirect('/')
            
def cart_home(request):
    all_items = Cart.objects.filter(user=request.user)
    flag = all_items.exists()
    return render(request,'cart/cart_home.html',{'items':all_items,'flag':flag})

def update_cart(request,id):
    p = request.POST.get('price')
    q = request.POST.get('qnt')
    p_id = request.POST.get('id')
    totalPrice = float(p)*int(q)
    Cart.objects.filter(id=p_id).update(quantity=q,totalprice=totalPrice)
    total_amount = Cart.objects.filter(user=request.user).aggregate(total=Sum('totalprice'))['total']or 0.0
    
    return JsonResponse({'status':True,'totalprice':totalPrice,'total_amount':total_amount})
    
        
def delete_cart_product(request,id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    messages.success(request,"Item Removed Successfully From Cart")
    return redirect('cart_home')

