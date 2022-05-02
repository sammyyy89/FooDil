"""foodil_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer import views as c_view
from restaurant import views as r_view

from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', c_view.Main, name="main"),

    path('customer/', c_view.Index, name="index"),
    path('customer/signup/', c_view.Signup, name='signup'),
    path('customer/login/', c_view.customer_login, name='login'),
    path('customer/logout', c_view.customer_logout, name='logout'),
    path('customer/order', c_view.order, name='order'),
    #path('customer/', include('django.contrib.auth.urls')), # login
    path('customer/store_detail/<int:restaurantID>/', c_view.Store_Detail, name='store_detail'),
    path('customer/cart/', c_view.Cart, name='cart'),
    path('customer/checkout/', c_view.Checkout, name='checkout'),
    path('customer/update_item/', c_view.updateItem, name="update_item"),
    path('customer/process_order/', c_view.processOrder, name='process_order'),
    path('customer/status/', c_view.Status, name='status'),
    path('customer/change_password/', c_view.change_password, name='change_password'),
    
    path('restaurant/', r_view.R_Index, name='r_index'),
    path('restaurant/signup/', r_view.R_Signup, name='r_signup'),
    path('restaurant/restaurant_login/', r_view.restaurant_login, name='r_login'),
    path('restaurant/logout', r_view.restaurant_logout, name='r_logout'),
    path('restaurant/menu/', r_view.menu, name='menu'),
    path('restaurant/add_menu/', r_view.Add_Menu, name='add_menu'),
    path('restaurant/update_item/<int:itemID>/', r_view.Update_Item, name='update_item'),
    path('restaurant/delete_item/<int:itemID>/', r_view.delete_item, name='delete_item'),
    path('restaurant/orders/', r_view.Orders, name='orders'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
