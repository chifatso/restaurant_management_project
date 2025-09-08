from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from django.db.utils import DatabaseError #to handle DB-specific error
from .serializers import MenuItemSerializer


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

    restaurant_address = getattr(settings, "RESTAURANT_ADDRESS", "Address not available")

    return render(request, "home/index.html",{
        "restaurant_name":restaurant_name,
        "restaurant_phone":restaurant_phone,
        "restaurant_address":restaurant_address
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

@api_view(["GET"]) #This API only supports get requests
def menu_list(request):
    """
    API endpoint that returns the restaurant's menu.
    For now, we use a hardcoded list of menu items

    """
    #Hardcoded menu (will later be replaced with DB query like Menu.objects.all())
    menu = [
        {"name":"Margherita Pizza", "description":"Classic pizza with cheese and tomato.", "price":8.99},
        {"name":"Caesar Salad", "description":"Crisp romaine with Caesar dressing and croutons.", "price":5.49},
        {"name":"Spaghetti Bolognese", "description":"Traditional pasta with rich meat sauce.", "price":10.99}
    ]

    #Serialize menu data -> JSON
    serializer = MenuItemSerializer(menu, many = True)

    #Return JSON response
    return Response(serializer.data)
