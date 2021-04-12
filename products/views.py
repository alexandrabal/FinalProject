from django.shortcuts import render
from django import urls

# Create your views here.
def view_all_products(request):
    products = []
    return render(request, 'products.html', {
        'name': name})