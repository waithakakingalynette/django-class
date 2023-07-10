from django.contrib import admin

# Register your models here.
from .models import Order
class Order_Admin(admin.ModelAdmin):
    list_display=('name','customer_id','quantity','price')

admin.site.register(Order, Order_Admin)


# customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#   basket = models.ForeignKey(Cart, on_delete=models.CASCADE)
#   shipment = models.OneToOneField(Delivery, on_delete=models.CASCADE)


    