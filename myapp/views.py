from django.shortcuts import render, redirect, HttpResponse
from .models import *
#^ Home 
def home(request):
    return render(request, 'index.html')
# 
def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')

def shopgrid(request):
    mid = Main_Category.objects.all()
    sid = Sub_category.objects.all()
    pid = Product.objects.all()
    sfid = Size_filter.objects.all()
    mid2 = request.GET.get('mid2')
    sid2 = request.GET.get('sid2')
    Bid = Brand_filter.objects.all()
    #print(Bid)
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
    }
    
    return render(request, 'shop-grid-ls.html', context)

def price_filter(request):
    if request.POST:
        min_num = request.POST['min_num']
        max_num = request.POST['max_num']
        pfid=Product.objects.filter(product_price__lte=max_num,product_price__gte=min_num)
        context = {
        "min_num": min_num,
        "max_num": max_num,
        "pfid": pfid
        }
        print(pfid)
        # print(min_num)
        # print(max_num)
        return render(request, 'shop-grid-ls.html',context)
    else:
        context = {
        "min_num": None,
        "max_num": None,
        "pfid": pfid
        }
        # print(min_num)
        # print(max_num)
        print(pfid)
        return render(request, 'shop-grid-ls.html',context)


def size_filter_product(request):
    sfid = Size_filter.objects.all()
    pid = Product.objects.all()
    size = request.POST.get('size')

    if size:
        pid = Product.objects.filter(Size_filter__size=size)
        l1 = []
        l1.extend(pid)
        # print("Filtered Products by size:", pid)
        context = {
            "sfid": sfid,
            "pid": l1 if size else pid,
            "size": size,
        }
    else:
        pid = Product.objects.all()
        print("All Products:", pid)
        context = {
            "sfid": sfid,
            "pid": pid,
            "size": size,
        }

    # print("Selected size:", size)
    return render(request, 'shop-grid-ls.html', context)

def Brand_filter_product(request):
    Bid = Brand_filter.objects.all()
    pid = Product.objects.all()
    brand = request.POST.getlist('brand')  # Get list of selected brand IDs (as strings)

    if brand:
        brand_ids = [int(b) for b in brand]  # Convert list of strings to integers
        pid = pid.filter(Brand_filter__id__in=brand_ids)
        #print('Filtered Products by brand:', pid)
        
    #print("Selected brands:", brand)
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