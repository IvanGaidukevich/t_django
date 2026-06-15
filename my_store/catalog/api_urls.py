from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.api_views import CategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('catalog/', include(router.urls)),
]
