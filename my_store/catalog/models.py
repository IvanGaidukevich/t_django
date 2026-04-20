from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("catalog:product_list_by_category", args=[self.slug])
    
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])
    


