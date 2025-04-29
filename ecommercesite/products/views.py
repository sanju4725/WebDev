from django.shortcuts import render, get_list_or_404
from .models import Catergory,Product

# Create your views here.
def product_list(request, category_slug):
    catergory = None
    products = Product.objects.filter(available=True)
    catergories = Catergory.objects.all()

    if category_slug:
        catergory = get_list_or_404(Catergory, slug=category_slug)
        products=products.filter(catergory=catergory)

    return render(request, 'products/product/list.html',{
        'category':catergory,
        'products':products,
        'catergories':catergories,
    })

def product_details()