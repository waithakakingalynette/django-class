from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    image = models.ImageField(upload_to='vendor_logo/', blank=False)

    def __str__(self):
        return self.name