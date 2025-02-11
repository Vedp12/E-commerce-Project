from django.shortcuts import render, redirect , HttpResponse
from .models import*

def home(request):
    return render(request, 'index.html')

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
    sfpid = request.GET.get('sfpid')  
    sfid = Size_filter.objects.all() 

    
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
        "sfid":sfid,
        "sid":sid
    }
    print(sfid)
    print(sfpid)
    print("Selected Main Category:", mid2)
    print("Selected Sub Category:", sid2)
    print("Filtered Products:", pid)  
    return render(request, 'shop-grid-ls.html',context)
    
def size_filter_product(request):
    sfid = Size_filter.objects.all() 
    size = request.POST.get('size')  
    pid = Product.objects.all()  
    
    l1 = []
    if size:
        pid = Product.objects.filter(Size_filter__size=size)
        l1.extend(pid)
        print("Filtered Products by size:", pid)
    else:
        pid = Product.objects.all()
        print("All Products:", pid)
    
    context = {
        "sfid": sfid,
        "pid":l1,
    }
    # print(sfid)
    print("Selected size:", size)
    return render(request, 'shop-grid-ls.html', context)

def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

def shop_single(request):
    return render(request, 'shop-single.html')