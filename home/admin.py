from django.contrib import admin
from . import models
from home.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)


admin.site.register(models.Product, ProductAdmin)