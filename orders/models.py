from django.db import models

class Order(models.Model):
    """ Model for the order table """
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    """ Model for the order items table """
    order = models.ForeignKey('orders.Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = 'orderitem'
