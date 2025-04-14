from django.urls import path

from product.views import (
    customer_list, 
    order_list, 
    product_list, 
    product_detail
)

urlpatterns = [
    path(
        route='product_list/', 
        view=product_list, 
        name='product_list'
    ),
    path(
        route='product_detail/<int:product_id>/',
        view=product_detail,
        name='product_detail'
    ),
    path(
        route='order_list/', 
        view=order_list, 
        name='order_list'
    ),
    path(
        route='customer_list/', 
        view=customer_list, 
        name='customer_list'
    )
]