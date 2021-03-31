from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {
        'brand': 'Swap it',
        'motto': 'Swap it',
        'product_list': [{
            'product_name': 'Long trousers',
            'price': 12,
            'size': 'S'
            }]
            })


def contact_view(request):
    return render(request, 'contact.html')
