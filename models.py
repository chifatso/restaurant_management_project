from django.db import models
from django.contrib.auth.models import User

#Rider Model

class Rider(models.Model):
    #Link each Rider to a Django User (OneToOne = each User can only be 1 Rider)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "rider_profile")

    #Rider-specific fields
    phone_number = models.CharField(max_length=15, unique=True)
    preferred_payment_method = models.CharField(
        max_length = 50,
        choices = [("card", "Card"), ("cash", "Cash"), ("wallet", "Wallet")],
        default = "cash"
    )
    default_pickup_location = models.CharField(max_length = 255, blank=True, null=True)
    profile_photo = models.ImageField(upload_to = "rider_profiles/", blank = True, null = True)

    def __str__(self):
        return f"Rider: {self.user.username}"
    
#Driver Model
class Driver(models.Model):
    #Link each Driver to a Django User
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "driver_profile")

    #Driver-specific fields
    phone_number = models.CharField(max_length = 15, unique = True)
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length = 50)
    number_plate = models.CharField(max_length = 20, unique = True)
    driver_license_number = models.CharField(max_length = 50, unique = True)

    availaibilty_status = models.BooleanField(default=True) #True=available, False = unavailable
    current_latitude = models.FloatField(blank = True, null = True)
    current_longitude = models.FloatField(blank = True, null = True)
    profile_photo = models.ImageField(upload_to = "driver_profiles/", blank=True, null=True)

    def __str__(self):
        return f"Driver: {self.user.username} - {self.number_plate}"