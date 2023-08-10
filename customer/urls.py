from django.urls import path

from .views import customer_upload_view
from .views import customer_detail
from .views import customer_list_view
from .views import customer_update_view

urlpatterns = [
    path("customer/upload", customer_upload_view, name="customer_upload_view"),
    path("products/list", customer_list_view, name="customer_list_view"),
    path("products/<int:id>/", customer_detail, name="customer_detail_view"),
    path("products/edit/<int:id>/",customer_update_view,name="customer_update")
]
