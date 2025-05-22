from django.shortcuts import render, get_object_or_404

from product.models import Product, OrderDetail, Order
from product.forms import ProductForm,OrderForm,OrderDetailForm

from product.services.products import ProductService
from product.services.customers import CustomerService
from product.services.orders import OrderService

from django.shortcuts import render, redirect
from django.contrib import messages

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
        
# NUEVAS VISTAS BASADAS EN CLASES
from django.views import View
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    CreateView
    )

from django.urls import reverse_lazy

class OrderDetailList(ListView):
    model = OrderDetail
    template_name = 'order_detail/list.html'
    context_object_name= 'orders'

class ProductList(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name= 'products'
class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name= 'product'
    pk_url_kwarg = 'product_id' #nombre con el que va a encontrar el ID en la ruta

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('product_list')

class ProductCreateView(View):
    def get(self, request):
        return render(request, 'products/create_product.html')
    
    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = float(request.POST.get('price'))
        stock = int(request.POST.get('stock'))

        Product.objects.create(
            name=name, 
            description=description, 
            price=price, 
            stock=stock)
        messages.success(request, 'Product created')
        
        return render(request, 'products/create_product.html')

#nuevo create v2 cortito
class ProductCreateViewV2(CreateView):
    form_class = ProductForm
    template_name = 'products/create_from_class.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['creador_de_productos'] = 'Creador de productos'
        print(context)
        return(context)
    
    def form_valid(self, form):
        messages.success(self.request, "Product created")
        return super().form_valid(form)
    
class OrderList(ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/create.html'
    success_url = reverse_lazy('order_create')

class OrderDetailCreate(CreateView):
    form_class = OrderDetailForm
    template_name = 'orders_detail/create.html'
    success_url = None

    def get_initial(self):
        # Devuelve valores precargados al formulario
        order_id = self.kwargs.get('order_id')
        return {'order': order_id} # order es el atributo de OrderDetailForm
    
    def get_success_url(self):
        # Esto hace que se quede en la misma pagina luego del exito de la llamada
        return reverse_lazy(
            'order_detail',
            kwargs={
                'order_id': self.kwargs.get('order_id')
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = get_object_or_404(Order, id=self.kwargs['order_id'])
        details = order.details.all()
        context['order'] = order
        details = [
            {
                "product": detail.product,
                "quantity": detail.quantity,
                "subtotal": detail.quantity * detail.product.price
            }
            for detail in details
        ]
        context['details'] = details
        context['total'] = sum(detail['subtotal'] for detail in details)
        return context