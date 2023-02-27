from recruitment_task_api.models.customer import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['_id', 'guid', 'is_active', 'username', 'first_name', 'last_name', 'created_at']