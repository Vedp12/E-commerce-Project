from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return redirect('signup')
        my_user = User.objects.create_user(username=uname, email=email, password=password)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login/')


@login_required(login_url='login/')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login/')
def account(request):
    return render(request, 'account.html')


@login_required(login_url='login/')
def cart(request):
    cart_items = Cart.objects.all()
    total_bill = sum(item.total_price for item in cart_items)
    context = {
        'cart': cart_items,
        'total_bill': total_bill,  
    }
    return render(request, 'cart.html', context)


def delete_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart')

def delete_Whole_cart(request):
    cart= Cart.objects.all()
    cart.delete()
    return redirect('cart')

def cart_add(request):
    quantity = request.POST.get('quantity')
    product_id = request.POST.get('product_id')
    product_price = request.POST.get('product_price')
    Cart.objects.add(quantity = quantity, product_price = product_price, product_id = product_id)
    return redirect('cart')


@login_required(login_url='login/')
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


@login_required(login_url='login/')
def about(request):
    return render(request,'about.html')


@login_required(login_url='login/')
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

@login_required(login_url='login/')

def update_cart(request):
    if request.method == "POST":
        cart_id = request.POST.get("cart_id")
        new_quantity = int(request.POST.get("quantity"))
        try:
            cart_item = Cart.objects.get(id=cart_id)
            cart_item.quantity = new_quantity
            cart_item.save()
            new_total = cart_item.total_price
            grand_total = sum(item.total_price for item in Cart.objects.all())
            return JsonResponse({
                "success": True,
                "new_total": new_total,
                "grand_total": grand_total
            })
        except Cart.DoesNotExist:
            return JsonResponse({"success": False, "error": "Cart item not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})

@login_required(login_url='login/')
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


@login_required(login_url='login/')
def search(request):
    Search_bar = request.POST.get('Search_bar')
    
    if Search_bar:
        pid = Product.objects.filter(product_name__icontains=Search_bar)
    else:
        pid = Product.objects.all()
    return render(request , 'shop-grid-ls.html', {'pid': pid} )


@login_required(login_url='login/')
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


@login_required(login_url='login/')
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


@login_required(login_url='login/')
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


@login_required(login_url='login/')
def shop_single(request):
    return render(request, 'shop-single.html')


