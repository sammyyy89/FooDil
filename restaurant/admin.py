from django.contrib import admin
from restaurant.models import Restaurant_Account, Menu
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

class AccountInline(admin.StackedInline):
    model = Restaurant_Account
    can_delete = False 
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

class Admin(admin.ModelAdmin):
    readonly_fields = ('restaurantID', ) # display restaurantID

class showID(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Restaurant_Account, Admin)
admin.site.register(Menu, showID)