from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=16, unique=True, verbose_name="Промокод")
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    valid_from = models.DateTimeField(verbose_name="Начало действия")
    valid_to = models.DateTimeField(verbose_name="Конец действия")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    