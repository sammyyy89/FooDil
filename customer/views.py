from multiprocessing.connection import deliver_challenge
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
import datetime

from urllib3 import HTTPResponse

from customer.decorators import unauthenticated_user
from customer.filters import StoreFilter, MenuFilter
from .forms import UserForm, SignupForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

from restaurant.models import Menu, Restaurant_Account
from .models import *

def Main(request):
    #logout(request)
    #messages.info(request, 'You are logged out.')
    return render(request, 'customer/main.html') 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def Index(request):
    return render(request, 'customer/index.html')

@unauthenticated_user
def Signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        s_form = SignupForm(request.POST)

        if form.is_valid() and s_form.is_valid():
            user = form.save()

            info = s_form.save(commit=False)
            info.user = user
            info.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, "Your account has been successfully created!")
            login(request, user)

           # return redirect('index')
    
    else:
        form = UserForm()
        s_form = SignupForm()

    context = {'form': form, 's_form': s_form }
    return render(request, 'customer/signup.html', context)

@unauthenticated_user
def customer_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect username or password.')

    context = {}
    return render(request, 'customer/login.html', context)

def customer_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def order(request):
    restaurants = Restaurant_Account.objects.all()

    store_filter = StoreFilter(request.GET, queryset=restaurants)
    restaurants = store_filter.qs

    context = {'restaurants':restaurants, 'store_filter': store_filter,} 
    return render(request, 'customer/order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def Store_Detail(request, restaurantID):
    #request.session['restaurantID'] = restaurantID 

    menu = Menu.objects.filter(restaurantID=restaurantID)
    store = Restaurant_Account.objects.get(restaurantID=restaurantID)

    item_filter = MenuFilter(request.GET, queryset=menu)
    menu = item_filter.qs 

    context = {'menu':menu, 'store':store, 'item_filter':item_filter}
    return render(request, 'customer/store_detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def Cart(request):
    print('카트 페이지')
    #restaurantID = request.session.get('restaurantID')
    customer = Customer_Account.objects.get(user=request.user.id)
    
    if request.user.is_superuser:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items
    else:
        order, created = Order.objects.get_or_create(username=customer, complete=False, )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems': cartItems, }
    return render(request, 'customer/cart.html', context)

"""
    if request.user.is_superuser:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items
    else:
        if request.method == 'POST':
            rid = request.POST['rid']
    
            order, created = Order.objects.get_or_create(username=customer, complete=False, restaurantId=rid)

        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems': cartItems, }
    return render(request, 'customer/cart.html', context)
   """

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def Checkout(request):
    #customer = request.user.id
    order, created = Order.objects.get_or_create(username=request.user.id, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'customer/checkout.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def updateItem(request):
    data = json.loads(request.body)

    itemId = data['itemId']
    action = data['action']
    rid = data['rid']

    print('itemId:', itemId)
    print('action:', action)
    print('rid:', rid)

    customer = Customer_Account.objects.get(user=request.user.id)
    item = Menu.objects.get(id=itemId)
    restaurant = Restaurant_Account.objects.get(restaurantID=rid)
    print('restaurant:', restaurant)
    
    order, created = Order.objects.get_or_create(username=customer, complete=False)
    items = order.orderitem_set.all()

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

    if not orderItem:
        print("카트 비어 있어요")
    else: # There are items in cart 
        if action == 'add':
            orderItem.quantity += 1
        elif action == "remove":
            orderItem.quantity -= 1
        
        orderItem.restaurantID = restaurant
        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    """    if not items: # 카트가 비어 있는 상태
        print('비어 있슈')
        if order.restaurantID == None: # 완전 첫 카트 담기
            order.restaurantID = restaurant
            order.save()
        else: # 담았다가 다 지운 상태라서 order.restaurantID에 값이 있음
            print("저장된 게 있음")
    else: # 카트에 물건이 있는 상태
        print("있어용")
        order.restaurantID = restaurant
        order.save()
"""


    return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    #username = request.user.username
    order, created = Order.objects.get_or_create(username=request.user.id, complete=False)
    total = data['form']['total']
    order.transaction_id = transaction_id
    order.complete = True

    #if total == float(order.get_cart_total):
        #order.complete = True
    order.save()

    DeliveryAddress.objects.create(
        username = Customer_Account.objects.get(user=request.user.id),
        order=order,
        address_1=data['form']['address_1'],
        address_2=data['form']['address_2'],
        city=data['form']['city'],
        state=data['form']['state'],
        zip_code=data['form']['zipcode'],
        delivery_option=data['form']['delivery_option'],
        note=data['form']['note'],
        status=data['form']['status']
    )
    return JsonResponse('Payment complete!', safe=False)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def Status(request):
    customer = Customer_Account.objects.get(user=request.user.id)
    info = DeliveryAddress.objects.filter(username=customer)

    context = {'info': info, }
    return render(request, 'customer/status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Password changed successfully!")
            # return redirect('index')
        else:
            #messages.error(request, 'Please correct the error and try again.')
            print('Error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/change_password.html', {'form': form})
