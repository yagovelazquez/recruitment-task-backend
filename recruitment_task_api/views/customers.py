from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from recruitment_task_api.models.customer import Customer
from recruitment_task_api.serializers.customer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = CustomerSerializer(data=data, many=True)
        else:
            serializer = CustomerSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        queryset = self.filter_queryset(self.get_queryset())
        if pk is not None:
               queryset = get_object_or_404(queryset, _id=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        pk = self.kwargs.get('pk')
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, _id=pk)
        return obj
