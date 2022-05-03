from tabnanny import verbose
from django.contrib import admin

from customer.models import Customer_Account, Order, OrderItem, DeliveryAddress
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

class AccountInline(admin.StackedInline):
    model = Customer_Account
    can_delete = False 
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)    

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class DeliveryAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('addedDate', )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Customer_Account)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
