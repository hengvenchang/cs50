from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("new",views.new),
    path("create",views.create),
    path("<int:room_id>",views.show)
]
