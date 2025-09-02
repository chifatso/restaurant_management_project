from django.db import models

# Create your models here.
class Menu(models.Model):
    """Represents a dish or Item available in the restaurant"""
    name = models.CharField(max_length=150) #CharField for limited characters
    description = models.TextField() #Textfield for longer text
    price = models.DecimalField(max_digits=10, decimal_places=2) #Like 199.22
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #What will display in the admin panels dropdowns or lists
        return str(self.name)