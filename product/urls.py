from django.urls import path

from product.views import product_list, order_list, customer_list

urlpatterns = [
    path(
        route='product_list/', 
        view=product_list, 
        name='product_list'
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