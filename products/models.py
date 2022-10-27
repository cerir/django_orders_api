from django.db import models

class Product(models.Model):
    """ Model for the product table """
    name = models.CharField(unique=True, max_length=255)
    price = models.DecimalField(max_digits=65535, decimal_places=2)
    stock_qty = models.IntegerField()

    class Meta:
        db_table = 'product'
