from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView

# Create your models here.
class Dish(models.Model):
    dish_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    dishes=models.ManyToManyField(Dish,through="OrderItem")
    status=models.CharField(max_length=50,default='recieved')

    def __str__(self):
        return self. customer_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default='recieved')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.order} - {self.dish} x{self.quantity}"








