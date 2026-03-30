from django.shortcuts import render, get_object_or_404
from catalog.models import Product



def product_list(request):
    products = Product.objects.filter(in_stock=True).order_by('name')
    return render(request, 'catalog/list.html', context={"products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'catalog/detail.html', context={"product": product})
