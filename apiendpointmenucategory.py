#home/serializers
from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    model = MenuCategory
    fields = ["name"]


#home/views.py
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

#API endpoint to fetch all menu categories
class MenuCategoryView(ListAPIView):
    queryset = MenuCategory.objects.all() #Get all categories
    serializer_class = MenuCategorySerializer #Converts to JSON

#home/urls.py
from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path("api/categories/", MenuCategoryListView.as_view(), name = "menu_categories")
]