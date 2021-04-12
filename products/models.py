from django.db import models
from django.contrib.auth import get_user_model
from final_project.models import CustomModel

AuthUserModel = get_user_model()

"""These are the product models, image, char field is a text base database column"""
# Create your models here.


ITEM_SIZES = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XS', 'Large'),
            ('XL', 'Large')
)


class Product(CustomModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.CharField(choices=ITEM_SIZES,max_length=2)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    quantity = models.IntegerField()


class Category(CustomModel):
    name = models.CharField(max_length=255)


class Image(CustomModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # for all foreign keys you don't need to name them with  _id
    image = models.ImageField(upload_to='product_commands')


class Review(CustomModel):
    name = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)


class QuestionAnswer(CustomModel):
    name = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
# one to many you define the relationship by adding the foreign key to the one model that has more -in this case
# one product can have more than one question but the question belongs to one product so one to many
