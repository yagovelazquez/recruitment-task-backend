from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from recruitment_task_api.views.customer_details import CustomerDetailsViewSet
from recruitment_task_api.views.customer_file import CustomerFileViewSet

from recruitment_task_api.views.customers import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'customers/(?P<id>\w+)/details', CustomerDetailsViewSet, basename='customer_details')
router.register(r'customers/(?P<id>\w+)/files', CustomerFileViewSet, basename='customer_files')

api_urls = [
     path('api/customers/<int:id>/', include(router.urls)),
]
api_urls += router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"api/", include(api_urls)),
]
