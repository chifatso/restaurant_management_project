from django.shortcuts import render
from django.conf import settings

# Create your views here.
def homepage(request):
    restaurant_name = settings.restaurant_name
    return render(request, "home/index.html", {"restaurant_name": restaurant_name})

def about(request):
    restaurant_name = settings.restaurant_name
    return render(request, "home/about.html", {"restaurant_name": restaurant_name})