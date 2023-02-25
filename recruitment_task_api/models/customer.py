from django.db import models

class Customer(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    guid = models.CharField(max_length=36)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)