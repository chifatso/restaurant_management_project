from rest_framework import serializers
from .models import Order, OrderItem

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
