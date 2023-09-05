from django import forms
from .models import Dish , Order,OrderItem

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'availability']




class OrderForm(forms.ModelForm):
     dishes = forms.ModelMultipleChoiceField(queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple)

     class Meta:
        model = Order
        fields = ['customer_name', 'dishes']
    
