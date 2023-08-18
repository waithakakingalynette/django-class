from django.db import models
# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 33)
    image = models.ImageField()
    phone_number = models.CharField(max_length = 10)
    date_created = models.DateTimeField(auto_now_add = True)
def __str__(self):
    return self.name