from django.contrib import admin
from .models import*
# # Register your models here.
admin.site.register(Main_Category)
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Size_filter)
admin.site.register(Brand_filter)
admin.site.register(Wishlist)