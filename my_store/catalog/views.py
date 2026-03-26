from django.shortcuts import render
from catalog.models import Product


def product_list(request):
    products = Product.objects.filter(in_stock=True).order_by('name')
    return render(request, 'catalog/list.html', context={"products": products})
