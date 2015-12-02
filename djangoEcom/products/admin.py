from django.contrib import admin
from products.models import Category, SubCategory, Products

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SubCategory)

		