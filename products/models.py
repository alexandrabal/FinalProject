from django.db import models
from django.contrib import get_user_model
from final_project import CustomModel

AuthUserModel = get_user_model


"""These are the product models, image, charfield is a textbase databasecolumn"""
# Create your models here.

class Product(CustomModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    color =models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    quantity = models.IntegerField()


ITEM_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
            )

class Category(CustomModel):
    name = models.CharField(max_length=255)

class Image(CustomModel):
    product_id = models.ForeignKey(Product,on_delete=CASCADE)
    image = models.ImageField(upload_to='product_commands')
    url = models.URLField(max_length=600)
