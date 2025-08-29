from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.about, name="about"),
    path("reservations/", views.reservations, name="reservations"),
    path("contact/", views.contact, name="contact"),
    path("menu/", views.menu_list, name="menu"),
    path("feedback/", views.feedback_view, name="feedback"),
    path("api/menu/", views.menu_list, name="menu_list"),
    
]