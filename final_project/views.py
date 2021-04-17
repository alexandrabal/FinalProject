from django.shortcuts import render

# render is a function from django.shortcuts that can take many parameters, among request and template_view

def homepage_view(request):
    if request.user.is_authenticated:
        print('user_id', request.user.id)

    return render(request, 'homepage.html', {
        'brand_name': 'Swap it',
        'motto': 'Swap it',
        'product_list': [{
            'product_name': 'Long trousers',
            'price': 12,
            'size': 'S'
            }]
            })

def view_all_products(request):
    products = []
    return render(request, 'products.html', {
        'name': name})

def contact_view(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')

