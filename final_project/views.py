from django.shortcuts import render
from products.models import Product

# render is a function from django.shortcuts that can take many parameters, among request and template_view

def homepage_view(request):
    if request.user.is_authenticated:
        print('user_id', request.user.id)
    products = Product.objects.all()[:5]
    # querying the database

    return render(request, 'homepage.html', {
        'brand_name': 'ESSE',
        'motto': 'Sustainable essentials',
        'product_list': products,
        "all_products": Product.objects.count()

        # 'size': products
            # 'product_name': 'Long trousers',
            # 'price': 12,
            # 'size': 'S'
            # }]
            })

def contact_view(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')

