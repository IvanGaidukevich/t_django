from django.contrib import admin
from django.urls import path
from catalog.views import product_detail, product_list

app_name = 'catalog'

urlpatterns = [
    path('', product_list, name="product_list"),
    path('<slug:category_slug>/', product_list, name="product_list_by_category"),
    path('catalog/<int:id>/<slug:slug>/', product_detail, name="product_detail"),
]
