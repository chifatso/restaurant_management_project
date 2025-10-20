from django.db import models
from products.models import Menu 
from .models import OrderStatus

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
    code = models.CharField(max_length = 20, unique = True) # generate code
    discount = models.DecimalField(max_digits = 5, decimal_places = 2) # discount amount
    active = models.BooleanField(default = True) # Whether the coupon is still valid

    def __str__(self):
        return self.code
    
    






