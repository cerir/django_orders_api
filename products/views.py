from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.conf import settings
from .serializers import ProductSerializer
from .models import Product


class ProductViewset(ModelViewSet):
    """
    Viewset to create, update, list and view products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer








