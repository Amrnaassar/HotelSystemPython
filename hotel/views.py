from django.shortcuts import render
from .models import booking
from .models import room
# Create your views here.
def Index(request):
    return render(request,'hotel/index.html',{})


def book (request):
     if request.method=="POST":
         addbook=booking()
         addbook.name=request.POST['name']
         addbook.id=request.POST['id']
         addbook.email=request.POST['email']
         addbook.phone=request.POST['phone']
         addbook.days=request.POST['days']
         addbook.roomnum=request.POST['roomnum']
         addbook.save()
     return render(request,'hotel/booking.html',{})

def home(request):
    return render(request,'hotel/home.html',{})
def cancel(request):
    if request.method == "POST":
        booking.objects.filter(ID=request.POST['id']).delete()

    return render(request,'hotel/cancel.html',{})