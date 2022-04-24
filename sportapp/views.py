from django.shortcuts import render,HttpResponse
from datetime import datetime
from sportapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def club(request):
    return render(request,"club.html")
def location(request):
    return render(request,"location.html")
def contact(request):
    if request.method=="POST":
        co =Contact()
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address= request.POST.get('address')
        gender= request.POST['Gender']
        sport=[]
        sport.append( request.POST.get('SPORT1'))
        sport.append( request.POST.get('SPORT2'))
        sport.append( request.POST.get('SPORT3'))
        sport.append( request.POST.get('SPORT4'))
        sport.append( request.POST.get('SPORT5'))
        co.name=name
        co.email=email
        co.phone=phone 
        co.address=address
        co.gender=gender
        co.sport=sport
        co.date=datetime.today()
        co.save()
        messages.success(request, 'Succesfully Register!')

    return render(request,"contact.html")