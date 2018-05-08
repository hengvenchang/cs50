from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.ForeignKey('PizzaName', on_delete=models.CASCADE)
    type = models.ForeignKey('PizzaType', on_delete=models.CASCADE,null='false')
    s_price = models.FloatField(null='false')
    l_price = models.FloatField(null='false')

class PizzaName(models.Model):
     name = models.CharField(max_length=255)

class PizzaType(models.Model):
    type = models.CharField(max_length=255)

class PizzaTopping(models.Model):
    topping = models.CharField(max_length=255)

class PizzaSize(models.Model):
     name = models.CharField(max_length=255)
     size = models.IntegerField()

class Pasta(models.Model):
     name = models.CharField(max_length=255)
     price = models.FloatField(null='false')

class Salads(models.Model):
     name = models.CharField(max_length=255)
     price = models.FloatField(null='false')

class DinnerPlatters(models.Model):
     name = models.CharField(max_length=255)
     s_price = models.FloatField(null='false')
     l_price = models.FloatField(null='false')

class Subs(models.Model):
     name = models.CharField(max_length=255)
     s_price = models.FloatField(null='false')
     l_price = models.FloatField(null='false')
