from django.db import models
from django.conf import settings
import helpers.billing


User = settings.AUTH_USER_MODEL

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f'{self.user.first_name} {self.user.last_name}'
    
    '''
        This method is called when the object is saved to the database.
        It creates a customer in Stripe when a new user is created.
    '''
    def save(self, *args, **kwargs):
        stripe_id = helpers.billing.create_customer(name=self.user.username, email=self.user.email, raw=False)
        self.stripe_id = stripe_id
        super().save(*args, **kwargs)