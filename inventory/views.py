from django.shortcuts import render
from .forms import Product_Upload_Form
# Create your views here.

def product_upload_view(request):
    form =Product_Upload_Form()
    return render(request,"inventory/product_upload.html",{"form":form})