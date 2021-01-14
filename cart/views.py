from django.shortcuts import render,redirect
from django.conf import settings
from datetime import date
# Create your views here.
from plays.models import Play, Viewing, Seat
from .models import Cart, Discount, Shipping


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    ship = Shipping.objects.all()
    context = {
    'cart': cart_obj,
    'ship':ship
    }
    return render(request, "carts/home.html", context)


def cart_update(request):
    print(request.POST)
#    play_id = request.POST.get('play_id') #gets play to put in basket
    view_id = request.POST.get('view_id')
    seat_id = request.POST.get('seat')
    # ship_id = request.POST.get('ship_id')

    #if play_id is not None:
    if view_id is not None:

        view_obj = Viewing.objects.get(id=view_id)
        seat_obj = Seat.objects.get(id=seat_id)
        # ship_obj = Shipping.objects.get(id=ship_id)



        #play_obj = Play.objects.get(id=play_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)


        if view_obj in cart_obj.views.all():
            #cart_obj.views.remove(view_obj)
            cart_obj.views.add(view_obj)
            cart_obj.seats.add(seat_obj)

            cart_obj.discount.add(add_discount(request))


        else:

            cart_obj.views.add(view_obj)
            cart_obj.seats.add(seat_obj)
            cart_obj.discount.add(add_discount(request))
        request.session['cart_items'] = cart_obj.views.count()


    #cart_obj.plays.remove(play_obj)
    return redirect('cart:home')

def cart_update_again(request):
    print(request.POST)
    ship_id = request.POST.get('ship')



    #if play_id is not None:
    if ship_id is not None:

        ship_obj = Shipping.objects.get(id=ship_id)

        print(ship_obj)

        #play_obj = Play.objects.get(id=play_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)


        if ship_obj in cart_obj.shipping.all():
            # cart_obj.shipping.remove(ship_obj)
            cart_obj.shipping.add(ship_obj)


        else:
            cart_obj.shipping.add(ship_obj)


        request.session['cart_items'] = cart_obj.views.count()


    #cart_obj.plays.remove(play_obj)
    return redirect('cart:home')

def add_discount(request):

    #1- OAP 2-child 3-none 4-as1 5-as2 6-hr
    if request.user.is_authenticated:
        # today = date.today()
        # birthday = request.user.date_of_birth
        # days_in_year = 365.2425
        age = age_calculator(request)

        if age >= 65 and request.user.agency_name == False:
            discount_obj = Discount.objects.get(pk=1)
            # return discount_obj
        elif age <= 18 and request.user.agency_name == False:
            discount_obj = Discount.objects.get(pk=2)
            # return discount_obj
        elif age >18 and age < 65 and request.user.agency_name == False:

            discount_obj = Discount.objects.get(pk=3)
            # return discount_obj
        elif request.user.agency_name == True:
            discount_obj = Discount.objects.get(pk=4)
            # return discount_obj
        else:
            discount_obj = Discount.objects.get(pk=3)
    else:
        discount_obj = Discount.objects.get(pk=3)

    return discount_obj



def age_calculator(request):
    today = date.today()
    birthday = request.user.date_of_birth
    days_in_year = 365.2425
    age = int((date.today() - birthday).days / days_in_year)
    print (age)
    return age
