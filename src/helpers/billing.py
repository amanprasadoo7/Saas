import stripe
from decouple import config

'''

    See your keys here: https://dashboard.stripe.com/apikeys
    If STRIPE_SECRET_KEY has initials of "sk_test_" then it's a test key
    If STRIPE_SECRET_KEY has initials of "sk_live_" then it's a live key    
    
    To test the script locally in python shell, run the following command:
    
    python manage.py shell
    
    from helpers.billing import *
    DJANGO_DEBUG
    stripe.api_key
    
'''

DJANGO_DEBUG = config('DEBUG', default=False, cast=bool)
stripe.api_key = config('STRIPE_SECRET_KEY', default='', cast=str)

if "sk_test_" in stripe.api_key and not DJANGO_DEBUG:
    raise ValueError("Stripe test key in production environment")

# stripe.Customer.create(
#   name="Aman",
#   email="aman@example.com",
# )

def create_customer(name='', email='', raw=False):
    response = stripe.Customer.create(
        name=name,
        email=email,
    )
    if raw:
        return response
    stripe_id = response.get('id')
    return stripe_id