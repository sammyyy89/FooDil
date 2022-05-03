from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from restaurant.models import *

class Customer_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_customer = models.BooleanField(default=True)
    is_restaurant = models.BooleanField(default=False)
    phoneNumberRegex = RegexValidator(regex = r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 15, unique = True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=50,
        choices=[('', 'Choose state'),('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Conneticut'),('DE', 'Delaware'),('DC', 'Dist. of Columbia'),('FL', 'Florida'),('GA', 'Georgia'),('GU', 'Guam'),('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MIN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nervada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utha'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')])
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    username = models.ForeignKey(Customer_Account, on_delete=models.SET_NULL, null=True)
    restaurantID = models.ForeignKey(Restaurant_Account, on_delete=models.SET_NULL, null=True)
    orderedDate = models.DateTimeField(auto_now_add=True)
    #isPaid = models.BooleanField(default=False)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username.user.username
        #return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    restaurantID = models.ForeignKey(Restaurant_Account, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Menu, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    addedDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(default=False, null=True, blank=True)

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total

    #def __str__(self):
        #return self.item.item

class DeliveryAddress(models.Model):
    username = models.ForeignKey(Customer_Account, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=50,
        choices=[('', 'Choose state'),('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Conneticut'),('DE', 'Delaware'),('DC', 'Dist. of Columbia'),('FL', 'Florida'),('GA', 'Georgia'),('GU', 'Guam'),('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MIN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nervada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utha'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')])
    zip_code = models.CharField(max_length=20)
    delivery_option = models.CharField(max_length=30, choices=[('Leave at door', 'Leave at door'), ('Hand it to me', 'Hand it to me')], default='Leave at door')
    addedDate = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, default=None, null=True, blank=True)
    status = models.CharField(max_length=30, choices=[('current status', 'current status'), ('Order Received', 'Order Received'), ('Preparing', 'Preparing'), ('Picked up', 'Picked up'), ('Delivered', 'Delivered')], default="current status")
    restaurantID = models.CharField(max_length=10, null=True, blank=True, default=0)

    def __str__(self):
        return self.address_1
