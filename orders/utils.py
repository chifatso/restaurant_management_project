import string
import secrets
from .models import Coupon
from datetime import date
from django.db.models import Sum
from .models import Order 

def generate_coupon_code(length = 10):
  """
  Generate a unique alphanumeric coupon code.
  -Uses the secrets module for cryptographically securing random generation
  -Checks against existing codes in the database to ensure uniqueness
  """
  # Define possible characters (uppercase letters + digits)
  characters = string.ascii_uppercase + string.digits

  while True: #Keep looping until a unique code is found
    #Generate a random string of the given length
    code = ''.join(secrets.choice(characters) for _ in range(length))

    #Check if code already exists in the Coupon table
    if not Coupon.objects.filter(code = code).exists():
      return code

def get_daily_sales_total(target_date):
    """
    Utility function to calculate the total sales for a given date.

    Args:
        target_date (date): A Python datetime.date object representing the day to calculate sales for.

    Returns:
        Decimal: Total amount of sales for that date. Returns 0 if no sales exist.
    """

    # 1️⃣ Filter all orders created on the target date.
    # The "__date" lookup extracts the date part from the DateTimeField 'created_at'.
    orders = Order.objects.filter(created_at__date=target_date)

    # 2️⃣ Use Django's aggregation to sum all total_price fields.
    result = orders.aggregate(total_sum=Sum('total_price'))

    # 3️⃣ Extract the total from the aggregation result.
    total_sales = result['total_sum'] or 0  # Use 0 if no sales found

    # 4️⃣ Return the total sales amount for the given date.
    return total_sales
    
