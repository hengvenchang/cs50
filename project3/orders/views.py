from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza,PizzaTopping,PizzaType,PizzaSize,Pasta,Subs,Salads,DinnerPlatters
from .models import Order
# from rest_framework import serializers
import json
# Create your views here.

def index(request):
    return render(request,'orders/orders.html')
def pizza(request):
    pizzas = Pizza.objects.all()
    toppings = PizzaTopping.objects.all()
    pizzaTypes = PizzaType.objects.all()
    # pizzas = serializers.serialize('json', self.get_queryset())
    # print(topping)
    context = {
        'pizzas':pizzas,
        'pizzaToppings':toppings,
        'PizzaType':pizzaTypes,
        'defaultType':'Regular'
    }
    print(pizzas[0].name.name)
    return render(request,'orders/ordersPizza.html',{'context':context})

def showMenu(request,name):
    global menu
    if(name == "pasta"):
        menu = Pasta.objects.all()
    elif(name == "subs"):
        menu = Subs.objects.all()
    elif(name == "salad"):
        menu = Salads.objects.all()
    elif(name == "dinner_platter"):
        menu = DinnerPlatters.objects.all()
    else:
        menu = None
    context = {
        'menus':menu
    }
    return render(request,'orders/orderCustom.html',{'context':context})
def order(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    user = request.user
    if request.POST.get("size"):
        size = PizzaSize.objects.filter(name=request.POST.get("size")).first()
    else:
        size = None
    newOrder = Order(name=name,customer=user,price=price,size=size)
    newOrder.save()
    return HttpResponse(newOrder.id)

def lists(request):
    orders = Order.objects.all().order_by('-created_at')
    context = {
        'orders':orders
    }
    return render(request,'orders/orderLists.html',{'context':context})
