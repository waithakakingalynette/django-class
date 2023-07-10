from django.db import models

# Create your models here.
class Basket(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  items = models.ManyToManyField(Product, through='BasketItem')

  class Meta:
    verbose_name = 'Basket'
    verbose_name_plural = 'Baskets'