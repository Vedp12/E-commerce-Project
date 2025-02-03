from django.shortcuts import render, redirect , HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')

def shopgrid(request):
    return render(request, 'shop-grid-ls.html')

def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

def shop_single(request):
    return render(request, 'shop-single.html')