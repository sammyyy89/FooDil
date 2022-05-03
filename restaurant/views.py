from ast import Del
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
import customer

from restaurant.models import Restaurant_Account, Menu
from .forms import MenuForm, R_UserForm, R_SignupForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

from .filters import MenuFilter
from customer.models import *
import json

def Main(request):
    #logout(request)
    #messages.info(request, 'You are logged out.')
    return render(request, 'customer/main.html') 

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def R_Index(request):
    return render(request, 'restaurant/index.html')

@unauthenticated_user
def R_Signup(request):
    if request.method == 'POST':
        form = R_UserForm(request.POST)
        s_form = R_SignupForm(request.POST, request.FILES)

        if form.is_valid() and s_form.is_valid():
            user = form.save()

            info = s_form.save(commit=False)
            info.user = user
            info.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            group = Group.objects.get(name='restaurant')
            user.groups.add(group)
            messages.success(request, "Your business account has been successfully created!")
            login(request, user)

            #return redirect('r_index')
    
    else:
        form = R_UserForm()
        s_form = R_SignupForm()

    context = {'form': form, 's_form': s_form }
    return render(request, 'restaurant/signup.html', context)

@unauthenticated_user
def restaurant_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('r_index')
        else:
            messages.info(request, 'Incorrect username or password.')

    context = {}
    return render(request, 'restaurant/restaurant_login.html', context)

def restaurant_logout(request):
    logout(request)
    return redirect('r_login')

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def menu(request):
    if request.user.is_superuser:
        rid = 1
    else:   
        rid = request.user.restaurant_account.restaurantID
    details=Menu.objects.filter(restaurantID=rid)    

    myFilter = MenuFilter(request.GET, queryset=details)
    details = myFilter.qs

    return render(request, 'restaurant/menu.html', {'data':details, 'myFilter': myFilter})

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def Add_Menu(request):
    form = MenuForm
    #display=Restaurant_Account.objects.get(restaurantID=restaurantID)
    #menu = {'restaurantID': request.user.restaurant_account.restaurantID }
    if request.user.is_superuser:
         return HttpResponse('Admin does not have a restaurant ID. Restaurant ID is required to add menu.')
    else:
        menu = {'restaurantID': request.user.restaurant_account.restaurantID }

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved successfully!")
            #return redirect('r_index')
        else:
            form=MenuForm()
    form = MenuForm(initial=menu)
    return render(request, 'restaurant/add_menu.html', {'form':form })

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def Update_Item(request, itemID):
    menu = get_object_or_404(Menu, id=itemID)
    form = MenuForm(request.POST or None, request.FILES or None, instance=menu)

    if form.is_valid():
        form.save()
        messages.success(request, "Updated successfully!")
    return render(request, 'restaurant/update_item.html', {'menu': menu, 'form': form})

def delete_item(request, itemID):
    item = Menu.objects.get(id=itemID)
    item.delete()
    return redirect('menu')

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def Orders(request):
    #info = DeliveryAddress.objects.filter()
    #orders = OrderItem.objects.filter(restaurantID=request.user.id)
    #rid = Restaurant_Account.objects.get(restaurantID=request.user.id)
    rid = request.user.restaurant_account.restaurantID

    info = DeliveryAddress.objects.filter(restaurantID=rid)
    orders = OrderItem.objects.filter(restaurantID=rid)

    items = OrderItem.objects.values('transaction_id').annotate(
        customer=F('order__username'),
        tid=F('transaction_id'),
        ordered=F('item')
    ).values('customer','tid', 'ordered')

    x = [item for item in items ]

    context = {'info': info, 'orders': orders, 'items': items}
    return render(request, 'restaurant/orders.html', context)

@login_required(login_url='r_login')
@allowed_users(allowed_roles=['admin', 'restaurant'])
def update_status(request):
    data = json.loads(request.body)
    transaction_id = data['form']['transaction_id']
    status = data['form']['status']

    print('tid:', transaction_id)
    print('status:', status)

    customer_status = DeliveryAddress.objects.get(transaction_id=transaction_id)

    customer_status.status = data['form']['status']
    customer_status.save()

    return JsonResponse("Status updated", safe=False)