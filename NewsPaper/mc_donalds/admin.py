from django.contrib import admin
from .models import Product, Order, Staff, ProductOrder, Country

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
admin.site.register(Staff)
admin.site.register(Country)
