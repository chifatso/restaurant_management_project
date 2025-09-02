from django.db import models
from products.models import Menu 

# Create your models here.
class Order(models.Model):
    """Represents a customer order"""
    customer_name = models.CharField(max_length = 100) #Using CharField for limited character length
    menu_item = models.ForeignKey(Menu, on_delete = models.CASCADE) #If Menu is deleted orders are deleted too.
    quantity = models.PositiveIntegerField(default = 1)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order #{self.id}-{self.customer_name}"

