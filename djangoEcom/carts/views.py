from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from products.models import Products, Variation
from carts.models import CartItem, Cart
import json

from django.contrib import messages


def cart(request):
    try:
        id = request.session['cart_id']
        cart = Cart.objects.get(id=id)

    except:
        id = None

    if id:
        cart.save()

        context = {'cart': cart}


    else:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}

    template = 'carts/cart.html'
    return render(request, template, context)


def add_ajax(request, slug):
    if request.is_ajax() and request.POST:
        print 'here'
        try:
            id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id

            id = new_cart.id
        cart = Cart.objects.get(id=id)
        product = Products.objects.get(slug=slug)

        product_var = []
        qty = request.POST['qty']
        for item in request.POST:
            category = item
            title = request.POST[category]
            try:
                v = Variation.objects.filter(product=product, category=category, title=title)
                product_var.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart_item.save()

        if len(product_var) > 0:
            cart_item.quantity = qty
            cart_item.line_total = int(cart_item.quantity) * int(cart_item.product.price)
            cart_item.save()

            request.session['cart_items'] = len(cart.cartitem_set.all())
            badge = len(cart.cartitem_set.all())

        new_data = json.dumps(badge)
        return HttpResponse(new_data, content_type='application/json')
    else:
        raise Http404


def add(request, slug):
    try:
        id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        id = new_cart.id

    cart = Cart.objects.get(id=id)
    product = Products.objects.get(slug=slug)

    product_var = []
    if request.method == 'POST':
        qty = request.POST['qty']
        for item in request.POST:
            category = item
            title = request.POST[category]
            try:
                v = Variation.objects.filter(product=product, category=category, title=title)
                product_var.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart_item.save()

        if len(product_var) > 0:
            cart_item.quantity = qty
            cart_item.line_total = int(cart_item.quantity) * int(cart_item.product.price)
            cart_item.save()

        return HttpResponseRedirect(reverse('cart'))
    raise Http404

def remove(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.cart = None
    cart_item.save()
    return HttpResponseRedirect(reverse('cart'))




