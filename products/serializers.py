from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product table
    """
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock_qty'
        )
