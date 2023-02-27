from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from recruitment_task_api.models.customer import Customer
from recruitment_task_api.models.customer_file import CustomerFile
from recruitment_task_api.serializers.customer_file import CustomerFileSerializer
from rest_framework.decorators import action


class CustomerFileViewSet(viewsets.ModelViewSet):
    queryset = CustomerFile.objects.all()
    serializer_class = CustomerFileSerializer

    def create(self, request, id=None, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=id)
        request.data["customer"] = customer.pk
        serializer = CustomerFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get_queryset(self):
        id = self.kwargs.get('id')
        if id:
            return CustomerFile.objects.filter(customer___id=id)
        else:
            return CustomerFile.objects.all()
        
    @action(url_path=r"(?P<file_id>\w+)/download", detail=False, methods=["get"])
    def download(self, request, id=None, file_id=None, *args, **kwargs):
        customer_file = get_object_or_404(CustomerFile, pk=file_id, customer=id)
        file_path = customer_file.file.path
        return FileResponse(open(file_path, 'rb'))    
        
 

