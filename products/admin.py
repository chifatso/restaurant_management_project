from django.contrib import admin
from .models import Menu


# Custom Admins
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','price','created_at']
    


# Register your models here.
admin.site.register(Item,ItemAdmin)