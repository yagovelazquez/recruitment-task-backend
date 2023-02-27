from rest_framework import serializers

from recruitment_task_api.models.customer_details import CustomerDetails


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['id', 'balance', 'picture', 'age', 'gender', 'email', 'phone', 'company', 'address', 'about', 'latitude', 'longitude']


class AddCustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['customer', 'balance', 'picture', 'age', 'gender', 'email', 'phone', 'company', 'address', 'about', 'latitude', 'longitude']

