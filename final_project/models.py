from django.db import models

'''class Meta- nested class, tells Django this is not a real class and to not bring it in as a table,
therefore it's an abstract class'''


class CustomModel(models.Model):
    class Meta:
        abstract=True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
