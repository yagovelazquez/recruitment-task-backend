from django.db import models
from recruitment_task_api.models.customer import Customer

class CustomerDetails(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.URLField(max_length=9999)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    about = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()