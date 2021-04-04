'''These are the order models'''
from django.db import models
from django.contrib import get_user_model
from final_project import CustomModel

AuthUserModel = get_user_model

# Create your models here.
class Order(CustoModel):
    billing_address_id = models.ForeignKey(Address)


class OrderProduct(CustoModel):
    order_id = models.ForeignKey(Product)
    product_id = models.ForeignKey(Product)
    quantity = models.IntegerField()


class UserOrder(CustoModel):
    user_id = models.ForeignKey(User)
    order_id = models.ForeignKey(Product)



