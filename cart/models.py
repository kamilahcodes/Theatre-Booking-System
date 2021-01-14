from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from plays.models import Play, Seat, Viewing
from decimal import Decimal


from django.shortcuts import render, redirect

User = settings.AUTH_USER_MODEL
# Create your models here.
class Discount(models.Model):
    name = models.CharField(max_length=120)
    value = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)

    def __str__(self):
        return str(self.name)

class Shipping(models.Model):
    types = [('Standard Shipping', 'Standard Shipping'), ('First Class', 'First Class'), ('Pick up', 'Pick up')]
    name = models.CharField(choices=types, default=None, null=True, max_length =100,)
    value = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)

    def __str__(self):
        return str(self.name)

class CartManager(models.Manager):


    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            print('Cart id exists')
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user

                cart_obj.save()
        else:
                cart_obj = Cart.objects.new(user=request.user)
                new_obj = True
                request.session["cart_id"] = cart_obj.id
        return cart_obj, new_obj


    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user

        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    #plays = models.ManyToManyField(Play, blank=True)
    views = models.ManyToManyField(Viewing, blank=True)
    seats = models.ManyToManyField(Seat, blank=True)
    discount = models.ManyToManyField(Discount, blank=True)
    shipping = models.ManyToManyField(Shipping, blank=True)

    playstotal = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    seattotal = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    discountvalue = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    shippingtotal = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)


    subtotal = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100,decimal_places=2)
    updated = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_view_cart(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        #plays = instance.plays.all()
        views = instance.views.all()
        total = 0
        for x in views:

        #for x in plays:
            total += Decimal(20.00)
        instance.playstotal = total

        instance.save()

m2m_changed.connect(m2m_view_cart,sender=Cart.views.through) #sender=Cart.plays.through)

def m2m_seat_cart(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':

        seats = instance.seats.all()

        total = 0


        for x in seats:
            total += x.price
        instance.seattotal = total

        instance.save()

m2m_changed.connect(m2m_seat_cart,sender=Cart.seats.through)

def m2m_discount_cart(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':

        discount = instance.discount.all()

        total = 0


        for x in discount:
            total += x.value
        instance.discountvalue = total

        instance.save()

m2m_changed.connect(m2m_discount_cart,sender=Cart.discount.through)
#
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':

        shipping = instance.shipping.all()

        total = 0


        for x in shipping:
            total += x.value
        instance.shippingtotal = total

        instance.save()

m2m_changed.connect(m2m_changed_cart_receiver,sender=Cart.shipping.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.subtotal = instance.playstotal + instance.seattotal
    instance.total = ((instance.subtotal)*instance.discountvalue) + instance.shippingtotal
    # instance.total = instance.subtotal #+seats #-discounts
pre_save.connect(pre_save_cart_receiver, sender=Cart)
