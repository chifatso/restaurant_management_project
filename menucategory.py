from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.name
    
#Run migrations in bash
#python manage.py makemigrations
#python manage.py migrate