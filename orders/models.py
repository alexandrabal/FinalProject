# These are the order models

from django.db import models
from django.contrib.auth import get_user_model
from final_project.models import CustomModel
from users.models import Address
from products.models import Product

AuthUserModel = get_user_model()

# Create your models here.

class Order(CustomModel):
    billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    # A user can have more than one order but an order only belongs to one user, each order has one user.
    product = models.ManyToManyField(Product, through='OrderProduct')


class OrderProduct(CustomModel):
    # only make a separate junction table for manytomany relationships
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # this table will include: id, order_id, stock, created_at, updated_at



