from rest_framework import serializers
from .models import Order, OrderItem
from .models import Coupon

# Nested serializer for the order items
class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['item_name', 'quantity']


# Main serializer for the order itself
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # nested data

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'total_price', 'items']

class CouponSerializer(serializers.ModelSerializer):
    """
    Serializer for Coupon model.
    Used to display coupon details after validation.
    """
    class Meta:
        model = Coupon
        fields = ['code', 'discount_percentage', 'valid_from', 'valid_until']
