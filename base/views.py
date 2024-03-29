from django.shortcuts import render, redirect
from .models import Room, Comments
from .forms import RoomForm


# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
def room(request, pk):
    room = Room.objects.get(id=pk)
    comments = Comments.objects.all()
    context = {'room': room,
               "comments": comments}
    return render(request, 'base/rooms.html', context)

