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
    mid = Main_Category.objects.all()
    sid = Sub_category.objects.all()
    pid = Product.objects.all()  # Initially get all products

    mid2 = request.GET.get('mid2')  # Get Main Category ID from request
    sid2 = request.GET.get('sid2')  # Get Subcategory ID from request

    # Filter subcategories based on the selected Main Category
    if mid2:
        sid = sid.filter(Main_Category_id=mid2)

    # Filter products based on the selected Subcategory
    if sid2:
        pid = pid.filter(Sub_category_id=sid2)

    context = {
        "mid": mid,
        "sid": sid,
        "pid": pid,  # Now pid is filtered correctly
        "mid2": mid2,
        "sid2": sid2,
    }

    print("Selected Main Category:", mid2)
    print("Selected Sub Category:", sid2)
    print("Filtered Products:", pid)  # Debugging output

    return render(request, 'shop-grid-ls.html', context)




def shopgrid1(request):
    return render(request, 'shop-grid-ls1.html')

def shop_single(request):
    return render(request, 'shop-single.html')