from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# Create profile automatically when a new User is created.
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

# Save profile when User is saved
@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
