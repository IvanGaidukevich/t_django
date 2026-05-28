from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User


ORDER_STATUS_CHOICES = (
    ('active', 'Активный'),
    ('completed', 'Выполненный'),
    ('canceled', 'Отмененный'),
)

class Order(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='active', verbose_name='Статус')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ № {self.id}'
    
    def get_total_cost(self):
        return sum(item.total_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'
    
    def total_price(self):
        return self.price * self.quantity


