from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout

# def login(request):
#     return render(request, 'login.html')
#* Signup

def signup(request):
    if request.POST:
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        #! Database  Connection
        Signup.objects.create(uname=uname, email=email, password=password)
        if password != confirm_password:
            return redirect('signup')
        return redirect('login')
    return render(request, 'signup.html')

#* Login
def login(request):    
    if request.POST:
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        print(uname, password)
        try:
            signid = Signup.objects.get(uname=uname, password=password)
            print(signid)
            if uname == None or password == None or signid.uname != uname or signid.password != password: 
                return redirect('login')
            else:
                return redirect('home')
        except Signup.DoesNotExist:
            return redirect('login')
    return render(request,"login.html")

def logoutpage(request):
    logout(request)
    return redirect('login')

#* Home
def home(request):
    return render(request, 'index.html')

#* Account
def account(request):
    return render(request, 'account.html')


#* Cart
def cart(request):
    cart_item = Cart.objects.all()
    print(cart_item)
    context={
        'cart': cart_item
    }
    return render(request, 'cart.html', context)

#* Add to Cart
def add_to_cart(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        cart_item, created = Cart.objects.get_or_create(
            product=product,
            defaults={
                'product_name': product.product_name,
                'product_image': product.product_image,
                'product_price': product.product_price,
                'quantity': 1
            }
        )
        if not created:
            cart_item.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('shopgrid')

#* About
def about(request):
    return render(request,'about.html')

#* Shop Grid
def shopgrid(request):
    mid  = Main_Category.objects.all()
    sid  = Sub_category.objects.all()
    pid  = Product.objects.all()
    sfid = Size_filter.objects.all()
    Bid  = Brand_filter.objects.all()
    mid2 = request.GET.get('mid2')
    sid2 = request.GET.get('sid2')
    wishlist_items = Wishlist.objects.values_list('product_id', flat=True)
    cart_item = Cart.objects.values_list('product_id', flat=True)
    
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
        "wishlist": wishlist_items, 
        "cart_item": cart_item,
    }
    return render(request, 'shop-grid-ls.html', context)

#* Wishlist
def wishlist(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        wishlist_item, created = Wishlist.objects.get_or_create(
            product=product,
            defaults={
                'product_name': product.product_name,
                'product_image': product.product_image,
                'product_price': product.product_price
            }
        )
        if not created:
            wishlist_item.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('shopgrid')


#* Search
def search(request):
    Search_bar = request.POST.get('Search_bar')
    
    if Search_bar:
        pid = Product.objects.filter(product_name__icontains=Search_bar)
    else:
        pid = Product.objects.all()
    return render(request , 'shop-grid-ls.html', {'pid': pid} )

#* Price Filter
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

#* Size Filter
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


#* Brand Filter
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
#* Shop Grid 1
def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

#* Shop Single
def shop_single(request):
    return render(request, 'shop-single.html')