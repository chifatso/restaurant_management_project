from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
    def validate_price(self, value):
        """
        Custom validation to ensure the price is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

