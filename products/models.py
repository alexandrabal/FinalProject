from django.db import models
from django.contrib import get_user_model
from final_project import CustomModel

AuthUserModel = get_user_model

"""These are the product models, image, charfield is a textbase databasecolumn"""
# Create your models here.

ITEM_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
)

class Product(CustomModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    color = models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    quantity = models.IntegerField()


class Category(CustomModel):
    name = models.CharField(max_length=255)

class Image(CustomModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # for all foreign keys you don't need to name them with  _id
    image = models.ImageField(upload_to='product_commands')
    url = models.URLField(max_length=600)

class Review(CustomModel):
    name = models.TextField()
    product = models.ForeignKey(Product)
    user = models.ForeignKey(AuthUserModel)

class QuestionAnswer(CustomModel):
    name = models.TextField()
    product = models.ForeignKey(Product)
    user = models.ForeignKey(AuthUserModel)
#     one to many you define the relationship by adding the foreign key to the one model that has more -in this case
# one product can have more than one question but the question belongs to one product so one to many







