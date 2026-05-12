from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from catalog.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('catalog:product_list')


@require_POST
def cart_remove(request, product_id):
    pass


def cart_detail(request):
    pass
# Create your views here.
