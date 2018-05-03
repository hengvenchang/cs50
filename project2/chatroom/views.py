from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
# Create your views here.
def index(request):
    rooms = Room.objects.order_by("title")
    context = {
    'user': request.user,
    'rooms': rooms,
    }
    print(request.user)
    return render(request,'chatroom/chatroom.html',{'context':context})
def new(request):
    context = {}
    return render(request,'chatroom/new.html',{'context':context})
def show(request,room_id):

    room = Room.objects.get(pk=room_id)
    context = {
    'room': room,
    }
    return render(request,'chatroom/room.html',{'context':context})
def create(request):
    room_title = request.POST.get("room_title")
    new_room = Room(title=room_title)
    new_room.save()

    new_page = './'+ str(new_room.id)
    return redirect(new_page)
