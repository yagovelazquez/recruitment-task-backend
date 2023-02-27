from rest_framework import serializers
from recruitment_task_api.models.customer_file import CustomerFile

class CustomerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFile
        fields = '__all__'
