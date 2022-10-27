from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product table
    """
    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email'
        )
