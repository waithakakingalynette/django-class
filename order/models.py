from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=32)
    customer_id = models.PositiveIntegerField()
    quantity= models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

# basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
# customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
# shipments = models.ManyToManyField(Shipment)