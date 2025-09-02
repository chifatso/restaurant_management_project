from django.contrib import admin
from .models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "menu_item", "quantity", "created_at")
    list_filter = ("created_at",)
    search_fields = ("customer_name",)

