from django.db import models
# from cart.models import Cart
# from order.models import Order


# Create your models here.
class Cart(models.Model):
    items_name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    number_of_items=models.PositiveIntegerField(default=1)
    discount=models.DecimalField(max_digits=8,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    description=models.TextField()
    