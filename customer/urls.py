from django.urls import path

from .views import customer_upload_view,customer_list_view,customer_detail,customer_update_view

urlpatterns = [
    path("customer/upload/", customer_upload_view, name="customer_upload_view"),
    path("customer/list/", customer_list_view, name="customer_list_view"),
    path("customer/<int:id>/", customer_detail, name="customer_detail_view"),
    path("customer/edit/<int:id>/",customer_update_view,name="customer_update")
]
