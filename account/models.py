from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Extend the built-in user model with extra fields.
class Profile(models.Model):
    # One-to-One link with django's default User.
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Extra fields for profile.
    phone_number = models.CharField(max_length = 15, blank = True, null = True)

    def __str__(self):
        # Display username when looking at this object in admin panel.
        return self.user.username
