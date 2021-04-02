from django.shortcuts import render


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


def contact_view(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')