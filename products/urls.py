from .views import ProductViewset
from rest_framework.routers import DefaultRouter

app_name = 'products'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', ProductViewset, basename="product")

urlpatterns = router.urls
