"""djangoEcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'products.views.index', name='index'),
    url(r'^products/$', 'products.views.products', name='products'),
    url(r'^product/(?P<slug>[\w-]+)/$', 'products.views.prod', name='prod'),
    url(r'^s/$', 'products.views.search', name='search'),

    url(r'cart/$', 'carts.views.cart', name='cart'),
    url(r'cart/(?P<slug>[\w-]+)/$', 'carts.views.add', name='add'),
    url(r'add_ajax/$', 'carts.views.add_ajax', name='add_ajax'),
    url(r'remove/(?P<id>[\w-]+)/$', 'carts.views.remove', name='remove'),

    url(r'^accounts/login/$', 'accounts.views.user_login', name='login'),
    url(r'^accounts/register/$', 'accounts.views.register', name='register'),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='logout'),

    url(r'^checkout/$', 'order.views.checkout', name='checkout'),

    url(r'^contact_us/$', 'contact.views.contact_us', name='contact_us'),

    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/post/(?P<id>[\w-]+)/$', 'blog.views.post', name='post'),
    url(r'^blog/edit_post/(?P<id>[\w-]+)/$', 'blog.views.edit_post', name='edit_post'),
    url(r'^blog/delete_post/(?P<id>[\w-]+)/$', 'blog.views.delete_post', name='delete_post'),
    url(r'^blog/add_post/$', 'blog.views.add_post', name='add_post'),

    url(r'^api/post_list/$', 'api.views.post_list', name='post_list'),
    url(r'^api/post_single/(?P<id>[\w-]+)/$', 'api.views.post_single', name='post_single'),

    url(r'^api/product_list/$', 'api.views.product_list', name='product_list'),
    url(r'^api/product_single/(?P<id>[\w-]+)/$', 'api.views.product_single', name='product_single'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = format_suffix_patterns(urlpatterns)
