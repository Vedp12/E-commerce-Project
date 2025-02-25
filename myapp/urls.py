from django.contrib import admin
from django.urls import path 
from myapp import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logoutpage,name='logout'),
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('account', views.account,name="account"),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('size_filter_product',views.size_filter_product,name='size_filter_product'),
    path('Brand_filter_product',views.Brand_filter_product,name='Brand_filter_product'),
    path('wishlist/<int:id>/', views.wishlist, name='wishlist'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='cart'),
    path('price_filter',views.price_filter,name='price_filter'),
    path('shopgrid1',views.shopgrid1,name='shopgrid1'),
    path('shop_single',views.shop_single,name='shop_single'),
]
