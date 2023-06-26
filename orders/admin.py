
from django.contrib import admin
from .models import Order, OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'last_name', 'first_name', 'order_total', 'is_ordered', 'created_at', 'updated_at')
    search_fields = ('order_number', 'last_name', 'first_name')
    ordering = ('order_number',)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'product_price', 'ordered', 'created_at', 'updated_at')
    search_fields = ('order', 'product')
    ordering = ('order',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
