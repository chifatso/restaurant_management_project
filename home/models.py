from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100) #Optional: name of the customer
    email = models.EmailField(blank = True) #Optional: all blank emails
    comments = models.TextField() #Feedback text
    created_at = models.DateTimeField(auto_now_add = True) #Timestamp

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'}"

class ContactSubmission(models.Model):
    # Stores user's name
    name = models.CharField(max_length = 100)

    # Stores user's email
    email = models.EmailField()

    # Timestamp of submission
    submitted_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return f"{self.name} - {self.email}"

class MenuCategory(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    has_delivery = models.BooleanField(default = False)
    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    """ Represents a daily special menu item in the restaurant"""
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    is_available = models.BooleanField(default = True)
    def __str__(self):
        return self.name

    @staticmethod
    def get_random_special():
        """
        Static method to fetch a random available daily special.
        Returns:
            A single DailySpecialInstance if available or None if no specials exist.
        """
        try:
            # Filter only available specials randomly order item
            special = DailySpecial.objects.filter(is_available = True).order_by('?').first()

            # Returns one random item, or None if no records exist
            return special
        except Exception as e:
            # Log or handle any unexpected errors
            print("Error fetching random dailt special:", e)
            return None









