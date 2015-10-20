from django.shortcuts import render, get_object_or_404
from products.models import Products, ProductImage


def index(request):
    return render(request, 'index.html')


def products(request):
    products = Products.objects.all()
    template = 'products/products.html'
    context = {'products': products}
    return render(request, template, context)


def prod(request, slug):
    product = get_object_or_404(Products, slug=slug)
    images = ProductImage.objects.filter(product=product)
    template = 'products/prod.html'
    context = {'product': product, 'images': images}
    return render(request, template, context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Products.objects.filter(title__icontains=q)
        template = 'products/search.html'
        context = {'query': q, 'products': products}
    else:
        template = 'products/products.html'
        context = {}
    return render(request, template, context)
