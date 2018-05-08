# from django.db import models
#
# # Create your models here.
# class Pizza(models.Model):
#     name = models.ForeignKey('PizzaName', on_delete=models.CASCADE)
#     type = models.ForeignKey('PizzaType', on_delete=models.CASCADE)
#     type = models.ForeignKey('PizzaPrice', on_delete=models.CASCADE)
#
# class PizzaName(models.Model):
#     name = models.CharField(max_length=255)
#
# class PizzaType(models.Model):
#     type = models.CharField(max_length=255)
#
#
# class PizzaPrice(models.Model):
#     size = models.CharField(max_length=255)
#     price = models.BigIntegerField()
#
#
# class PizzaOrders(models.Model):
#     name = models.BigIntegerField()
#     size = models.BigIntegerField()
#     topping = models.CharField(max_length=255)
#     price = models.bigint()
