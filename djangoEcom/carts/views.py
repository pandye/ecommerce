from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404, get_object_or_404
from django.core.urlresolvers import reverse
from products.models import Products
from carts.models import CartItem, Cart
from django.http import JsonResponse
import json

def cart(request):
    request.session.set_expiry(0)
    try:
        id = request.session['cart_id']
        cart = get_object_or_404(Cart, id=id)
        request.session['cart_items'] = len(cart.cartitem_set.all())
        item_val = request.session['cart_items']
    except:
        cart = False
        item_val = 0

    if item_val ==0:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}
    else:
        context = {'cart': cart}
    if cart and cart.active:
        cart = cart
        cart.total = 0
        for item in cart.cartitem_set.all():
            cart.total += item.line_total
            cart.save()

    template = 'carts/cart.html'
    return render(request, template, context)


def add_ajax(request):
    if request.is_ajax() and request.POST:
        try:
            id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id
            id = new_cart.id

        slug = request.POST['slug']
        qty = request.POST['qty']
        
        cart = get_object_or_404(Cart, id=id)
        product = get_object_or_404(Products, slug=slug)

        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart_item.save()
        cart_item.quantity = qty
        cart_item.line_total = int(cart_item.quantity) * int(cart_item.product.price)
        cart_item.save()

        request.session['cart_items'] = len(cart.cartitem_set.all())
        response_data = len(cart.cartitem_set.all())
        print response_data
        return HttpResponse(json.dumps(response_data), content_type='application/json')


def remove(request, id):
    cart_item = get_object_or_404(CartItem, id=id).delete()
    return HttpResponseRedirect(reverse('cart'))




