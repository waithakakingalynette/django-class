from django.contrib import admin

# Register your models here.
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
  list_display = ('created_at', 'updated_at', 'items')
