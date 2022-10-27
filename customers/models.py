from django.db import models

class Customer(models.Model):
    """ Model for the customer table """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'customer'
