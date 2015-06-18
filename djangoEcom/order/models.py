from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User)
    cart = models.ForeignKey('carts.Cart')
    shipping_address = models.ForeignKey('accounts.Address', related_name='shipping_address')
    billing_address = models.ForeignKey('accounts.Address', related_name='billing_address')