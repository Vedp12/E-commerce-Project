from django.contrib import admin
from django.urls import path 
from myapp import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.loginPage,name='login'),
    path('logout',views.logoutpage,name='logout'),
    path('home',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('cart_add',views.cart_add,name='cart_add'),
    path('delete_cart/<int:id>/',views.delete_cart,name='delete_cart'),
    path('delete_Whole_cart',views.delete_Whole_cart,name='delete_Whole_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),  
    path('account', views.account,name="account"),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('size_filter_product',views.size_filter_product,name='size_filter_product'),
    path('Brand_filter_product',views.Brand_filter_product,name='Brand_filter_product'),
    path('wishlist/<int:id>/', views.wishlist, name='wishlist'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='cart'),
    path('price_filter',views.price_filter,name='price_filter'),
    path('shop/<int:product_id>/', views.shop_single, name='shop_single'), 
]
