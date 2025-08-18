from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_views
from rest_framework.response import response
from .models import Restaurant
from django.db.utils import DatabaseError #to handle DB-specific errors


# Create your views here.
#Homepage view with error handing
def homepage(request):
    try:
        #Try and get restaurant name from database
        restaurant = Restaurant.objects.first()
        restaurant_name = restaurant.name if restaurant else settings.restaurant_name
        restaurant_phone = restaurant.phone if restaurant else settings.restaurant_phone
    except DatabaseError:
        #if DB connection/query fails use a fallback
        restaurant_name = settings.restaurant_name
        restaurant_phone = settings.restaurant_phone

    return render(request, "home/index.html", {
        "restaurant_name": restaurant_name,
        "restaurant_phone": restaurant_phone,
        })

def about(request):
    try:
        restaurant = Restaurant.objects.first()
        restaurant_name = restaurant.name if restaurant else settings.restaurant_name
    except DatabaseError:
        restaurant_name = settings.restaurant_name
    return render(request, "home/about.html", {"restaurant_name": restaurant_name})

def reservations(request):
    return render(request, "home/reservations.html")