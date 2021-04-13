from django.shortcuts import render
from products.models import Product

# Create your views here.
def view_all_products(request):
    products = []
    return render(request, 'products.html', {
        'name': name})

