'''These are the order models'''
from django.db import models
from django.contrib import get_user_model
from final_project import CustomModel

AuthUserModel = get_user_model

# Create your models here.

class Order(CustomModel):
    billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    user= models.OneToManyField('UserOrder')
# A user can have more than one order but an order only belongs to one user, each order has one user.
    product =models.ManyToManyField(Product, through='OrderProducts', related_name='product')


class OrderProduct(CustomModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class UserOrder(CustomModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Product, on_delete=models.CASCADE)


# this table will include: id, user_id,order_id, stock, price, created_at, updated_at
# Since django adds automatically the id, you don't need to specify user_id but can just put in the user as a foreign
# key, and django will add the user id
# doing user = models.ForeignKey(User, on_delete=models.CASCADE) means you create a relationship between this model and
# User model using the user attribute. Therefore Django will generate user_id column in the database.



