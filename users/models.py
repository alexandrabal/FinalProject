from django.db import models
from django.contrib.auth import get_user_model
from utils.constants import BILLING_ADDRESS, SHIPPING_ADDRESS
from final_project.models import CustomModel

AuthUserModel = get_user_model()
"This represents the usermodels, user model default from django added in a variable"
# Create your models here - ORM converting class objects into django columns

class Address(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, null = False)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)


    class Types(models.IntegerChoices):
        SHIPPING = SHIPPING_ADDRESS
        BILLING = BILLING_ADDRESS
    type = models.IntegerField(choices=Types.choices, null=False, default=SHIPPING_ADDRESS)








