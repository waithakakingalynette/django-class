from django.contrib import admin

# Register your models here.
from .models import View_Order
class View_Order_Admin(admin.ModelAdmin):
    list_display=('name','price','quantity','image','customer_id')

admin.site.register(View_Order,View_Order_Admin)