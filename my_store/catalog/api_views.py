from rest_framework import viewsets, mixins
from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.filter(in_stock=True)
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category_slug = self.request.query_params.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs
