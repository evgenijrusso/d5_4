from django.contrib import admin
from .models import Product, Order, Staff, ProductOrder

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
admin.site.register(Staff)
