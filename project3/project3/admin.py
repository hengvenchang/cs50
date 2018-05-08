from django.contrib import admin
# from orders.models import PizzaName,PizzaType,PizzaPrice,Pizza
from menu.models import *
from orders.models import Order,PizzaOrders
# admin.site.register([PizzaName,PizzaType,PizzaPrice,Pizza])
admin.site.register([PizzaName,PizzaType,Pizza,PizzaTopping,PizzaSize,Pasta,Salads,Subs,DinnerPlatters])
admin.site.register([Order,PizzaOrders])
# admin.site.register(PizzaType)
