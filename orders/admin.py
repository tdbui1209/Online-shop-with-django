from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'address',
                    'city', 'paid', 'created', 'updated', 'status', 'payment_method']
    list_filter = ['paid', 'created', 'updated', 'status']
    inlines = [OrderItemInline]
    list_editable = ['status', 'paid']

admin.site.register(Order, OrderAdmin)
