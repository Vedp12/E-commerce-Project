from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Wishlist, Product, Main_Category, Sub_category, Size_filter, Brand_filter
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request,'about.html')

def shopgrid(request):
    mid = Main_Category.objects.all()
    sid = Sub_category.objects.all()
    pid = Product.objects.all()
    sfid = Size_filter.objects.all()
    mid2 = request.GET.get('mid2')
    sid2 = request.GET.get('sid2')
    Bid = Brand_filter.objects.all()
    wishlist = None
    if request.method == 'POST':
        wishlist = Wishlist.objects.all()
        l1=[]
        for i in wishlist:
            l1.append(i.pid)
        print(l1)
        print(wishlist)
        print(pid)
    if mid2:
        sid = sid.filter(Main_Category_id=mid2)
    if sid2:
        pid = pid.filter(Sub_category_id=sid2)
    context = {
        "mid": mid,
        "sid": sid,
        "pid": pid,
        "mid2": mid2,
        "sid2": sid2,
        "sfid": sfid,
        "Bid": Bid,
        "wishlist": wishlist,
    }    
    return render(request, 'shop-grid-ls.html', context)


def wishlist(request, id):
    if request.method == 'POST':
        pid = Product.objects.get(id=id)
        wishlist, created = Wishlist.objects.get_or_create(
            product=pid,
            product_name=pid.product_name,
            product_image=pid.product_image,
            product_price=pid.product_price
        )
        if created:
            wishlist.save()
        else:
            wishlist.delete()
        context = {
            "wishlist": wishlist
        }
        return render(request, 'shop-grid-ls.html', context)
    else:
        return redirect('shopgrid')

def remove_wishlist(request, id):
    pid = Product.objects.get(id=id)
    wishlist_item = Wishlist.objects.filter(product_id=id).first()
    
    if wishlist_item:
        wishlist_item.delete()
    
    return redirect('shopgrid')


def search(request):
    Search_bar = request.POST.get('Search_bar')
    
    print(Search_bar)
    if Search_bar:
        pid = Product.objects.filter(product_name__icontains=Search_bar)
    else:
        pid = Product.objects.all()
    return render(request , 'shop-grid-ls.html', {'pid': pid} )

def price_filter(request):
    if request.POST:
        min_num = request.POST['min_num']
        max_num = request.POST['max_num']
        pid = Product.objects.filter(product_price__lte=max_num, product_price__gte=min_num)
        context = {
        "min_num": min_num,
        "max_num": max_num,
        "pid": pid
        }
        return render(request, 'shop-grid-ls.html', context)
    else:
        context = {
        "min_num": None,
        "max_num": None,
        "pid": pid
        }
        return render(request, 'shop-grid-ls.html', context)

def size_filter_product(request):
    sfid = Size_filter.objects.all()
    pid = Product.objects.all()
    size = request.POST.get('size')

    if size:
        pid = Product.objects.filter(Size_filter__size=size)
        l1 = []
        l1.extend(pid)
        
        context = {
            "sfid": sfid,
            "pid": l1 if size else pid,
            "size": size,
        }
    else:
        pid = Product.objects.all()
        
        context = {
            "sfid": sfid,
            "pid": pid,
            "size": size,
        }

    return render(request, 'shop-grid-ls.html', context)

def Brand_filter_product(request):
    Bid = Brand_filter.objects.all()
    pid = Product.objects.all()
    brand = request.POST.getlist('brand')  

    if brand:
        brand_ids = [int(b) for b in brand]  
        pid = pid.filter(Brand_filter__id__in=brand_ids)
    
    context = {
        'Bid': Bid,
        'pid': pid,
        'brand': brand
    }

    return render(request, 'shop-grid-ls.html', context)

def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

def shop_single(request):
    return render(request, 'shop-single.html')