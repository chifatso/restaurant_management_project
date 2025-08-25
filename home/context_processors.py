from django.conf import settings

def restaurant_info(request):
    return {
        "restaurant_opening_hours": getattr(settings, "RESTAURANT_OPENING_HOURS", "")
    }