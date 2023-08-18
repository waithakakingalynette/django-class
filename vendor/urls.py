from django.urls import path
from.views import vendor_upload_view,vendor_detail_view,vendor_list,edit_vendor_view
urlpatterns=[
    path("vendor/upload/",vendor_upload_view,name="vendor_upload_view"),
    path("vendor/list/",vendor_list,name="vendor_list"),
    path("vendor/<int:id>",vendor_detail_view,name="vendor_detail_view"),
    path('/vendor/edit/<int:id>/',edit_vendor_view,name='edit_vendor_view')
]