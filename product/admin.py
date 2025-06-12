from django.contrib import admin
from product.models import Product, Customer, Order, OrderDetail, Category, OrderDetailAuditLog

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'image')
    list_filter = ('name', 'category')
    search_fields = ('name', 'stock')

    actions = ['update_price_15']

    #aca me quede

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date') 

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')

@admin.register(OrderDetailAuditLog)
class OrderDetailAuditLogAdmin(admin.ModelAdmin):
    list_display = ['order_detail', 'product_name', 'quantity', 'timestamp', 'action']
    readonly_fields = list_display
