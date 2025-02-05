from django.contrib import admin
from django.urls import path 
from myapp import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('about',views.about,name='about'),
    path('shopgrid',views.shopgrid,name='shopgrid'),
    path('shopgrid1',views.shopgrid1,name='shopgrid1'),
    path('shop_single',views.shop_single,name='shop_single'),
]
