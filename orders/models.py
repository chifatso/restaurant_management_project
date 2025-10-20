from django.db import models
from products.models import Menu 
from .models import OrderStatus
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    """Represents a customer order"""
    customer_name = models.CharField(max_length = 100) #Using CharField for limited character length
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders') 
    menu_item = models.ForeignKey(Menu, on_delete = models.CASCADE) #If Menu is deleted orders are deleted too.
    quantity = models.PositiveIntegerField(default = 1)
    status = models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null = True) # Links the order model to order status model
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order #{self.id}-{self.customer_name}"

class OrderStatus(models.Model):
    name = models.CharField(max_length = 100, unique = True) # Stores the status name (must be unique e.g. "Pending", "Completed")

    def __str__(self):
        return self.name

class Coupon(models.Model):
    """
    Represents a discount coupon that users can apply to their orders.
    """

    code = models.CharField(max_length=50, unique=True)  # Coupon code, e.g., "WELCOME10"
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)  # e.g., 0.10 for 10% discount
    is_active = models.BooleanField(default=True)  # Can be turned off by admin
    valid_from = models.DateField()  # When the coupon becomes valid
    valid_until = models.DateField()  # When the coupon expires

    def __str__(self):
        return f"{self.code} ({self.discount_percentage * 100}% off)"
    
    







