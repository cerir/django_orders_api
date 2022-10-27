from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem


class OrderViewset(ModelViewSet):
    """
    Viewset to create, update, list and view orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('customer',)

class OrderItemViewset(ModelViewSet):
    """
    Viewset to create, update, list and view order items
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        """
        Override the create method to ensure the product stock qty is adjusted
        """
        orderitem_data = serializer.validated_data
        product = orderitem_data['product']
        qty = orderitem_data['qty']

        # Adjust the stock quantity
        product.stock_qty -= qty
        product.save()

        # Create the order item on our database
        serializer.save()





