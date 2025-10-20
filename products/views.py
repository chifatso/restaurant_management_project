from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MenuItemSerializer
from .models import Menu
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def menu_page(request):
    #Fetch all menu items from DB
    menu_items = Menu.objects.all()

    #Pass items to the template
    return render(request, "products/menu.html", {"menu_items":menu_items})
class MenuItemPagination(PageNumberPagination):
    """
    Pagination class for Menu Items.
    Limits the number of items returned per page.
    """
    page_size = 10  # Return 10 items per page
    page_size_query_param = 'page_size'  # Allow clients to override this value

class MenuItemSearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to search for menu items by name.
    Supports query parameter ?search=<term>
    Example: /api/menu/search/?search=pizza
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagination

    # Enables filtering/searching functionality
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # Search by 'name' field (case-insensitive)



