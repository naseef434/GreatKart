from itertools import product
from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from django.forms import DateField
from store.models import Product
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItemModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity 

    def __str__(self):
        return self.product  