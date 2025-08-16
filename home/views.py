from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_views
from rest_framework.response import response
from .models import Restaurant

# Create your views here.
def homepage(request):
    restaurant_name = settings.restaurant_name
    return render(request, "home/index.html", {"restaurant_name": restaurant_name})

def about(request):
    restaurant_name = settings.restaurant_name
    return render(request, "home/about.html", {"restaurant_name": restaurant_name})