from django.urls import path

from product.views import (
    customer_list,
    order_list, 
    ProductList,
    ProductDetail,
    ProductDelete,
    ProductCreateView,
    ProductCreateViewV2
)

urlpatterns = [
    path(
        route='product_list/', 
        view=ProductList.as_view(), 
        name='product_list'
    ),
    path(
        route='product_detail/<int:product_id>/',
        view=ProductDetail.as_view(),
        name='product_detail'
    ),
    path(
        route='product_delete/<int:product_id>/',
        view=ProductDelete.as_view(),
        name='product_delete'
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
    ),
    path(
        route='create_product/', 
        view=ProductCreateViewV2.as_view(), 
        name='create_product'
    )
]