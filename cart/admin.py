from django.contrib import admin
from .models import Cart, Discount, Shipping
# Register your models here.
admin.site.register(Cart)
admin.site.register(Discount)
admin.site.register(Shipping)
