#serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver

#Rider Registration Serializer
class RiderRegistrationSerializer(serializers.ModelSerializer):
    #Extra Rider fields
    phone_number = serializers.CharField(required = True)
    preferred_payment_method = serializers.CharField(required = True)
    default_pickup_location = serializers.CharField(required = False, allow_blank = True)
    profile_photo = serializers.ImageField(required = False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number", "preferred_payment_method", "default_pickup_location", "profile_photo"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        #Extract Rider-specific fields before creating User
        phone_number = validated_data.pop("phone_number")
        preferred_payment_method = validated_data.pop("preferred_payment_method")
        default_pickup_location = validated_data.pop("default_pickup_location")
        profile_photo = validated_data.pop("profile_photo", None)

        #Create Django User (password is automatically hashed)
        user = User.objects.create_user(**validated_data)

        #Create Rider profile linked to User
        Rider.objects.create(
            user = user,
            phone_number = phone_number,
            preferred_payment_method = preferred_payment_method,
            default_pickup_location = default_pickup_location,
            profile_photo = profile_photo,
        )

        return user
    
#Driver Registration Serializer
class DriverRegistrationSerializer(serializers.ModelSerializer):
    #Extra Driver fields
    phone_number = serializers.CharField(required = True)
    vehicle_make = serializers.CharField(required = True)
    vehicle_model = serializers.CharField(required = True)
    number_plate = serializers.CharField(required = True)
    driver_license_number = serializers.CharField(required = True)
    profile_photo = serializers.ImageField(required = False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number", "vehicle_make", "vehicle_model", "number_plate", "driver_license_number", "profile_photo"]
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        #Extract Driver-specific fields before creating User
        phone_number = validated_data.pop("phone_number")
        vehicle_make = validated_data.pop("vehicle_make")
        vehicle_model = validated_data.pop("vehicle_model")
        number_plate = validated_data.pop("number_plate")
        driver_license_number = validated_data.pop("driver_license_number")
        profile_photo = validated_data.pop("profile_photo", None)

        user = User.objects.create_user(**validated_data)

        #Create Driver profile linked to User
        Driver.objects.create (
            user = user,
            phone_number = phone_number,
            vehicle_make = vehicle_make,
            vehicle_model = vehicle_model,
            number_plate = number_plate,
            driver_license_number = driver_license_number,
            profile_photo = profile_photo,

        )

        return user
    
#views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RiderRegistrationSerializer, DriverRegistrationSerializer

#Rider Registration API
class RiderRegistrationView(APIView):
    def post(self, request):
        serializer = RiderRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Rider registered successfully",
                "username": user.username,
                "email": user.email
            }, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
#Driver Registration API
class DriverRegistrationView(APIView):
    def post(self, request):
        serializer = DriverRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message":"Driver registered successfully",
                "username": user.username,
                "email": user.email
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#urls.py
from django.urls import path
from .views import RiderRegistrationView, DriverRegistrationView

urlpatterns = [
    path("api/register/rider/", RiderRegistrationView.as_view(), name = "register_rider"),
    path("api/register/driver/", DriverRegistrationView.as_view(), name = "register_driver"),
]
        