from django.shortcuts import render
from django.conf import settings

# Create your views here.
def homepage(request):
    restaurant_name = settings.restaurant_name
    return render(request, "index.html", {"restaurant_name": restaurant_name})
