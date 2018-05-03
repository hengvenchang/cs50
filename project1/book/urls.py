from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("<int:book_id>",views.show),
    path("search", views.search),
]
