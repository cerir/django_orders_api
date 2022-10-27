from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order item table
    """

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'product',
            'qty'
        )

    def to_representation(self, instance):
        """To display the details of the user"""
        response = super().to_representation(instance)
        response["product"] = ProductSerializer(instance.product).data
        return response

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order table
    """
    order_date = serializers.DateTimeField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'order_date',
            'customer',
            'items'
        )
