from django.contrib import admin

# Register your models here.
from .models import Order
class Order_Admin(admin.ModelAdmin):
    list_display=('name','price','quantity','customer_id')

admin.site.register(Order,Order_Admin)