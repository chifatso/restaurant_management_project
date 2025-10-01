import string
import secrets
from .models import Coupon

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
    
