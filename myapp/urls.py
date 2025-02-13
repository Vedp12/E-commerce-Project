from django.contrib import admin
from django.urls import path 
from myapp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('size_filter_product',views.size_filter_product,name='size_filter_product'),
    path('Brand_filter_product',views.Brand_filter_product,name='Brand_filter_product'),
    path('price_filter',views.price_filter,name='price_filter'),
    path('shopgrid1',views.shopgrid1,name='shopgrid1'),
    path('shop_single',views.shop_single,name='shop_single'),
]
