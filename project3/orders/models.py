from django.db import models
from .choice import STATUS_CHOICES
from menu.models import *
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null='false')
    price = models.FloatField(null='false')
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE,null='true')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True,null='false')

class PizzaOrders(models.Model):
    name = models.ForeignKey(PizzaName, on_delete=models.CASCADE,null='false')
    size = models.CharField(max_length=255)
    topping = models.CharField(max_length=255)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE,null='false')
