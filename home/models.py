from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=10)
    product_desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)