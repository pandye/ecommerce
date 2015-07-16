from django.contrib import admin
from products.models import Category, Products, ProductImage, Variation

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ProductImage)
admin.site.register(Variation)

