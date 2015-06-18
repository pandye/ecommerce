from django.db import models
from products.models import Products, Variation


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    product = models.ForeignKey('products.Products')
    variations = models.ManyToManyField('products.Variation', null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.0, decimal_places=2, max_digits=65)
    notes = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    total = models.DecimalField(default=0.0, decimal_places=2, max_digits=65)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.id