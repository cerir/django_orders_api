from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.conf import settings
from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewset(ModelViewSet):
    """
    Viewset to create, update, list and view customers
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer






