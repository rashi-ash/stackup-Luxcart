from django.contrib import admin
from.models import Product, Cart

admin.site.register(Product)

class CartMixin(admin.ModelAdmin):
    list_filter = ('user',)

admin.site.register(Cart, CartMixin)

