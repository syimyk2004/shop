from django.contrib import admin
from . models import Category, Product, Favorite, Order, Order_product


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(Order_product)