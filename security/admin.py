from django.contrib import admin
from security.models import Order, Payment, User

from django.contrib.auth.models import Group

admin.site.site_title = "Tshafutshe Admin Portal"
admin.site.site_header = "Tshafutshe Dashboard"
admin.site.index_title = "Welcome to Tshafutshe Admin"

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_admin',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'first_name', 'last_name', 'is_ordered', 'order_number', 'order_total', 'currency', 'status', 'date_ordered',)
    list_filter = ('is_ordered', 'status', 'date_ordered')
    search_fields = ('email', 'first_name', 'last_name', 'order_number',)
    list_per_page = 20
    ordering = ('-date_ordered',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('user__email', 'payment_id',)
    list_per_page = 20
    ordering = ('-created_at',)
    list_editable = ('status',)