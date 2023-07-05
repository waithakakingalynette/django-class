from django.db import models

# Create your models here.
class View_Order(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.TextField()
    image = models.ImageField()
    customer_id = models.PositiveIntegerField()