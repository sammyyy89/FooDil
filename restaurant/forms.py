from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import restaurant
from .models import Restaurant_Account, Menu

CATEGORY = (
            ('', 'Choose category'),
            ('Appetizer', 'Appetizer'),
            ('Entree', 'Entree'),
            ('Drink', 'Drink'),
            ('Dessert', 'Dessert'), 
            ('Side', 'Side')
)


class R_UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class R_SignupForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your RESTAURANT NAME'}))
    image = forms.ImageField(required=False)
    phone = forms.CharField(required=True)
    website = forms.URLField(required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Italian, Thai, Korean, Chinese, Japanese, ...'}))
    hours = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'e.g. Mon - Fri 11:00 am - 10 pm'}))

    class Meta:
        model = Restaurant_Account
        fields = ('name','phone', 'image', 'website', 'country', 'hours')

class MenuForm(forms.ModelForm):
    item = forms.CharField(required=True)
    itemImage = forms.ImageField(required=False, label='Item Image')
    price = forms.DecimalField(required=True)
    category = forms.ChoiceField(choices=CATEGORY)
    class Meta:
        model = Menu
        fields = ('restaurantID','item', 'itemImage', 'price', 'category')





