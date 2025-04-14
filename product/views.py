from django.shortcuts import render, get_object_or_404

from product.models import Product

from product.services.products import ProductService
from product.services.customers import CustomerService
from product.services.orders import OrderService


# Create your views here.
def product_list(request):
    all_products = ProductService.get_all()

    return render(
        request, 
        'products/list.html',
        dict(
            products= all_products,
        )
    )

def product_detail(request, product_id):
    product = get_object_or_404(Product, id= product_id)

    return render(
        request,
        'products/detail.html',
        dict(
            products= product,
        )
    )

def order_list(request):
    all_orders = OrderService.get_all()
    return render(
        request,
        'orders/list.html',
        dict(
            orders= all_orders,
        )
    )

def customer_list(request):
    all_customers = CustomerService.get_all()
    return render(
        request, 
        'customers/list.html',
        dict(
            customers= all_customers,
        )
    )
        