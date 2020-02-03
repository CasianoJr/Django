from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['seller',
                    'name', 'slug', 'timestamp']
    list_editable = ['slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
