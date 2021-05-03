from .models import Product
from django.shortcuts import render


def view_all_products(request):
    products = Product.objects.all()
    # this objects function is used to take all the products from the list and show them

    return render(request, 'products/products.html', {
        "products": products
    #variable from the html template for product in products
    })


