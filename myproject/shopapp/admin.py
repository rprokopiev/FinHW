from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'reg_date', 'isactive']
    ordering = ['name']
    readonly_fields = ['reg_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Personal Data',
            {
                'description': 'Personal Data of the customer',
                'fields': ['phone', 'email', 'address'],
            }
        ),
        (
            'Application Data',
            {
                'classes': ['collapse'],
                'fields': ['reg_date', 'isactive'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'price', 'quantity', 'add_date']
    fields = ['prod_name', 'price', 'quantity', 'add_date', 'description', 'image']
    readonly_fields = ['add_date', 'description', 'image']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_date', 'amount']
    ordering = ['customer', 'order_date', 'amount']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

