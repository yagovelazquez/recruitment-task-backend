from django.contrib import admin
from django.urls import include, path, re_path

from recruitment_task_api.views.customers import HelloWorldView


api_urls = [
    path(r"hello", HelloWorldView.as_view(), name="me"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"api/", include(api_urls)),
]
