from django.db import models

class CustomModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''abstract = True property is the reason why this class/model is abstract, not the Meta class'''
'''tells Django this is not a real class and to not bring it in as a table, therefore it's ana abstract class'''




