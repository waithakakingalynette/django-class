from django.contrib import admin
from vendor.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'image')

admin.site.register(Vendor, VendorAdmin)