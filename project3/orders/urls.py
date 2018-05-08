from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('order', views.order),
    path('pizza', views.pizza),
    path('lists', views.lists),
    path('<slug:name>', views.showMenu),

]
