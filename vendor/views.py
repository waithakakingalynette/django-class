from django.shortcuts import render
from.forms import VendorUploadForm
from vendor.models import Vendor
from django.shortcuts import redirect
# Create your views here.
def vendor_upload_view(request):
    form =VendorUploadForm()
    return render(request,"vendor/vendor_upload.html",{"form":form})

def vendor_list(request):
    vendor= Vendor.objects.all()
    return render(request,"vendor/vendor_list.html",{"vendor":vendor})

def vendor_detail_view(request):
    vendor= Vendor.objects.all()
    return render(request,"vendor/vendor_detail.html",{"vendor":vendor})

def edit_vendor_view(request,id):
    vendor=Vendor.objects.get(id=id)
    if request.method=="POST":
        form=VendorUploadForm(request.POST,instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_detail_view',id=vendor)
        else:
            form=VendorUploadForm(instance=vendor)
            return render(request,'vendor/edit_vendor.html',{'form':form})
