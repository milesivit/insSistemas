from django.contrib import admin
from product.models import Product, Customer, Order, OrderDetail

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'image')
    list_filter = ('name',)
    search_fields = ('name', 'stock')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date') 

@admin.register(OrderDetail)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity') 
