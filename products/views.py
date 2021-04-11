from django.shortcuts import render


# Create your views here.
def view_all_products():
    products = []
    return render(request, 'products.html', {'products': products})
# why don't we give here the data from the json?
