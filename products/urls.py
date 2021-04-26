from django.urls import path
from .views import view_all_products

urlpatterns = [
    path('', view_all_products, name='products'),
]



