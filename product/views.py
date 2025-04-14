from django.shortcuts import render

from product.services.products import ProductService
from product.services.customers import CustomerService


# Create your views here.
def product_list(request):
    all_products = ProductService.get_all()
    return render(
        request, 
        'products/list.html',
        {
            'products' : all_products
        }
        )

def order_list(request):
    return render(request, 'orders/list.html')

def customer_list(request):
    all_products = CustomerService.get_all()
    return render(
        request, 
        'customers/list.html',
        {
            'customers' : all_products
        }
        )
        