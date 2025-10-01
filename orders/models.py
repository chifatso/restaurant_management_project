from django.db import models
from products.models import Menu 

# Create your models here.
class Order(models.Model):
    """Represents a customer order"""
    customer_name = models.CharField(max_length = 100) #Using CharField for limited character length
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
    



