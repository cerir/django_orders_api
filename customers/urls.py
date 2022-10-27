from .views import CustomerViewset
from rest_framework.routers import DefaultRouter

app_name = 'products'

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'', CustomerViewset, basename="customer")

urlpatterns = router.urls
