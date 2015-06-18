from django.shortcuts import render
from accounts.forms import AddressForm


def checkout(request):
    form = AddressForm()
    template = 'order/checkout.html'
    return render(request, template, {'form': form})