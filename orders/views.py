from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon
from .serializers import CouponSerializer

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

class CouponValidationView(APIView):
    """
    API endpoint to validate a coupon code.
    Expects a POST request with 'code' in the body.
    """

    def post(self, request):
        # Retrieve coupon code from request data
        code = request.data.get('code', '').strip()

        # Check if code was provided
        if not code:
            return Response({'error': 'Coupon code is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Try to get the coupon object from DB
            coupon = Coupon.objects.get(code__iexact=code)  # Case-insensitive match
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_404_NOT_FOUND)

        # Check coupon validity
        today = timezone.now().date()
        if not coupon.is_active:
            return Response({'error': 'This coupon is no longer active.'}, status=status.HTTP_400_BAD_REQUEST)

        if today < coupon.valid_from:
            return Response({'error': 'This coupon is not yet valid.'}, status=status.HTTP_400_BAD_REQUEST)

        if today > coupon.valid_until:
            return Response({'error': 'This coupon has expired.'}, status=status.HTTP_400_BAD_REQUEST)

        # If valid, serialize and return success message
        serializer = CouponSerializer(coupon)
        return Response({
            'message': 'Coupon is valid!',
            'discount_percentage': float(coupon.discount_percentage),
            'coupon_details': serializer.data
        }, status=status.HTTP_200_OK)

