from django.urls import path
from .views import cart_upload_view,add_to_cart,remove_cart_item,cart_list
# from.import views
urlpatterns= [
    path("cart/upload/", cart_upload_view,name='product_get_view'),
    # path('cart/', cart_list, name='cart_list'),   
    path('cart/add_to_cart/',add_to_cart, name='cart_list'),
    path('cart/list/', cart_list, name='cart_list'),
    path('cart/remove/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    
    ]