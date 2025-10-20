from django.urls import path
from .views import *

urlpatterns = [
    path('api/orders/history/', OrderHistoryView.as_view(), name='order-history'),
    

]
