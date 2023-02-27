from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from recruitment_task_api.models.customer_details import CustomerDetails
from recruitment_task_api.serializers.customer_details import AddCustomerDetailsSerializer, CustomerDetailsSerializer


class CustomerDetailsViewSet(viewsets.GenericViewSet):

    def get(self, request, id=None):
        queryset = CustomerDetails.objects.select_related('customer').filter(customer___id=id).first()
        if not queryset:
            return Response(status=204)
        serializer = CustomerDetailsSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, id=None):
        serializer = AddCustomerDetailsSerializer(data={"customer": id, **request.data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, id=None):
        queryset = get_object_or_404(CustomerDetails.objects.select_related('customer'), customer___id=id)
        serializer = CustomerDetailsSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        queryset = get_object_or_404(CustomerDetails.objects.select_related('customer'), customer___id=id)
        queryset.delete()
        return Response(status=204)
