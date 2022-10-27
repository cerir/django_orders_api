from .views import OrderViewset, OrderItemViewset
from rest_framework.routers import DefaultRouter

app_name = 'orders'

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'order', OrderViewset, basename="order")
router.register(r'items', OrderItemViewset, basename="orderitem")

urlpatterns = router.urls
