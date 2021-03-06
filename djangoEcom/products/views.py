from django.shortcuts import render, get_object_or_404, HttpResponse
from products.models import Products, Category, SubCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def index(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'index.html', context)


def products(request):
    categorys = Category.objects.all()

    product_list = Products.objects.all()
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    print categorys
    print products
    context = {'products': products, 'categorys': categorys}
    return render(request, 'products/products.html', context)


def prod(request, slug):
    product = get_object_or_404(Products, slug=slug)
    context = {'product': product}
    return render(request, 'products/prod.html', context)


def rating(request):
    if request.is_ajax() and request.POST:
        slug = request.POST['slug']
        product = get_object_or_404(Products, slug=slug)
        product_rate =  product.rating
        rate = request.POST['rate']
        new_rating = round(((product_rate+float(rate))/2), 1)
        product.rating = new_rating
        product.save()
        response_data = new_rating
        return HttpResponse(json.dumps(response_data), content_type='application/json')


def category(request, slug):
    categorys = Category.objects.all()

    category = get_object_or_404(Category, slug=slug)
    sub_cat = SubCategory.objects.filter(category=category)
    products = Products.objects.filter(sub_category=sub_cat)
    print category, sub_cat, products
    context = {'categorys': categorys, 'products': products}
    return render(request, 'products/products.html', context)


def sub_cat(request, slug):
    categorys = Category.objects.all()

    sub_cat = get_object_or_404(SubCategory, slug=slug)
    products = Products.objects.filter(sub_category=sub_cat)
    print sub_cat, products
    context = {'categorys':categorys, 'products': products}
    return render(request, 'products/products.html', context)


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
