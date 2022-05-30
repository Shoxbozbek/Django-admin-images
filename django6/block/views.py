from django.shortcuts import render
from .models import Home, Imege


def home(request):
   
    py = Home.objects.all(),
    image = Imege.objects.all()
    
    extend = {
        "home":py,
        "image":image
    }
    
    return render(request, 'home.html', extend)


def about(request):
    return render(request, 'about.html')