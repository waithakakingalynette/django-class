from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
      display_list = ('PAYMENT_METHOD', 'STATUS_CHOICES', 'payment_method','amount','date','status','description')
admin.site.register(Payment,PaymentAdmin)