from django.db import models

from recruitment_task_api.models.customer import Customer

class CustomerFile(models.Model):
    CATEGORY_CHOICES = (
        ('invoice', 'Invoice'),
        ('receipt', 'Receipt'),
        ('notes_to_customer', 'Notes to customer'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='customer_files/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
