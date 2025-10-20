from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderHistoryView(generics.ListAPIView):
    """
    API endpoint for retrieving the logged-in user's past orders.
    Only authenticated users can access it.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # user must be logged in

    def get_queryset(self):
        # Only show orders belonging to the logged-in user
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
