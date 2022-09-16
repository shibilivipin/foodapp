from itertools import product
from math import prod
from django.shortcuts import render,redirect,get_object_or_404
# from request import request
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_details(request, tot=0, count=0, cart_items=None):
    try:
        ct=cartlist.objects.get(user = request.user)
        ct_items = (items.objects.filter(cart=ct, active=True))

        for i in ct_items:
            tot +=(i.prodt_name.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci':ct_items, 't':tot, 'cn':count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    print(request.user.id)
    prod = products.objects.get(id = product_id)
    try:
        ct = cartlist.objects.get(cart_id = c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id = c_id(request), user = request.user)
        ct.save()
       
    try:
        c_items=items.objects.get(prodt_name=prod, cart=ct)
        if c_items.quantity < c_items.prodt_name.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt_name=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')



def minus_cart(request, product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id = product_id)
    c_items = items.objects.get(prodt_name=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id = product_id)
    c_items = items.objects.get(prodt_name=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')

    

