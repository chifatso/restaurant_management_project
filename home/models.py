from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100) #Optional: name of the customer
    email = models.EmailField(blank = True) #Optional: all blank emails
    comments = models.TextField() #Feedback text
    created_at = models.DateTimeField(auto_now_add = True) #Timestamp

    def __str__(self):
        return f"Feedback from {self.name or 'Anonymous'}"