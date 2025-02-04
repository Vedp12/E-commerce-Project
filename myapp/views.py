from django.shortcuts import render, redirect , HttpResponse
from .models import*
# Create your views here.
def home(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')

def shopgrid(request):
    mid=Main_Category.objects.all()
    sid=Sub_category.objects.all()
    pid=Product.objects.all()
    mid2=request.GET.get('mid2') 
    sid2=request.GET.get("sid2")
    context={
    "mid":mid,   
    "sid":sid,   
    "pid":pid,   
    "mid2":mid2,   
    }
    print(mid2)
    print(sid2)
    return render(request, 'shop-grid-ls.html',context)


def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

def shop_single(request):
    return render(request, 'shop-single.html')