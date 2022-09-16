from tkinter import CASCADE
from django.db import models
from shop.models import *
from django.contrib.auth.models import User

# Create your models here.
class cartlist(models.Model):
    cart_id = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.cart_id


class items(models.Model):
    prodt_name = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active=models.BooleanField(default=True)
    

    def __str__(self):
        return self.prodt_name

        
    def total(self):
        return self.prodt_name.price * self.quantity
