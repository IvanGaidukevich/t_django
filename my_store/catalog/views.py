from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from cart.forms import CartAddProductForm



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(in_stock=True, category=category).order_by('name')
    else:
        products = Product.objects.filter(in_stock=True).order_by('name')
    return render(request, 'catalog/list.html', 
                  context={"products": products, 
                           "categories": categories, 
                           "category": category})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    cart_product_form = CartAddProductForm()

    return render(request, 'catalog/detail.html', context={"product": product, 
                                                           "cart_product_form": cart_product_form})
