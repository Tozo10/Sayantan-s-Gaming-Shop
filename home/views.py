from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")
def abouts(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def contacts(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        name = request.POST.get('Name', '')
        phone = request.POST.get('Phone', '')
        desc = request.POST.get('desc', '')
        if name and email and phone and desc:
           contact = Contact(email=email, name=name, phone=phone, desc=desc, date=datetime.today())
           contact.save()
           messages.success(request, "Your message has been sent!")
        
        
       
        
        
    return render(request, "contact.html")