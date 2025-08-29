from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    #Define fields for each menu item
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits = 6, decimal_places = 2)