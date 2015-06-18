from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoEcom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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

    url(r'^checkout/$', 'order.views.checkout', name='checkout'),

    url(r'^contact_us/$', 'contact.views.contact_us', name='contact')
)
