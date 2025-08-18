from django.urls import path
from .views import *

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.about, name="about"),
    path("reservations/", views.reservations, name="reservations"),
    path("contact/", views.contact, name="contact"),
    
]