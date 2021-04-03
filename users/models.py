from django.db import models
from django.contrib.auth import get_user_model
from utils.constants import BILLING_ADDRESS, SHIPPING_ADDRESS

AuthUserModel = get_user_model()

# Create your models here - ORM converting class objects into django columns
class Address(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, null = False)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)

    class Types(models.IntegerChoices):
        SHIPPING = SHIPPING_ADDRESS
        BILLING = BILLING_ADDRESS
    type = models.IntegerField(choices=Types.choices, null=False, default=SHIPPING_ADDRESS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





