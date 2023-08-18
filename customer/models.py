from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def register_customer(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def is_exist(self):
        return Customer.objects.filter(email=self.email).exists()

   