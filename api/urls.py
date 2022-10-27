
from django.urls import include, re_path
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# urls
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/products/', include(('products.urls'), namespace='products')),
    re_path(r'^api/customers/', include(('customers.urls'), namespace='customers')),
    re_path(r'^api/orders/', include(('orders.urls'), namespace='orders'))
]

urlpatterns= tuple(urlpatterns)