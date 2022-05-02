from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

#from django.utils.html import mark_safe

CHOICES=[
('', 'Choose category'),
('Appetizer', 'Appetizer'),
('Entree', 'Entree'),
('Drink', 'Drink'),
('Dessert', 'Dessert'), 
('Side', 'Side')
]

class Restaurant_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=True)
    restaurantID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 12, unique = True)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        #return self.user.username
        return str(self.restaurantID)

class Menu(models.Model):
    restaurantID = models.ForeignKey(Restaurant_Account, on_delete=models.CASCADE, default=None, null=True)
    item = models.CharField(max_length=100)
    itemImage = models.ImageField(upload_to='images/', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=20,
        choices=CHOICES)
    
    def __str__(self):
        return self.item

