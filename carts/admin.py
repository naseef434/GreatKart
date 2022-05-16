from django.contrib import admin
from .models import Cart,CartItemModel
# Register your models here.



class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date')

class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ('product','cart','quantity','is_active')

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItemModel,CartItemModelAdmin)
