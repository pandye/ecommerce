from django.shortcuts import render, get_object_or_404
from products.models import Products, ProductImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'index.html')


def products(request):
    product_list = Products.objects.all()
    paginator = Paginator(product_list, 2)
    page = request.GET.get('page')
    print page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {'products': products}
    return render(request, 'products/products.html', context)


def prod(request, slug):
    product = get_object_or_404(Products, slug=slug)
    images = ProductImage.objects.filter(product=product)
    context = {'product': product, 'images': images}
    return render(request, 'products/prod.html', context)


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
        context = {}
    return render(request, 'products/products.html', context)
