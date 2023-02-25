from django.db import models

class Customers(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    guid = models.CharField(max_length=36)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)