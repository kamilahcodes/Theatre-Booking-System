from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
from cart.models import Cart
from .models import Play, Viewing, Seat
from reviews.models import Review



#change slider to home page, add album to play list
def play_list(request):
    queryset = Play.objects.all()
    context = {
        'plays':queryset
    }

    return render(request,"plays/list.html", context)

def home_slider(request):
    queryset = Play.objects.all()
    context = {
        'plays':queryset
    }

    return render(request,"home.html", context)





class ViewDetailDateView(DetailView):
    queryset = Viewing.objects.all()
    template_name = "plays/seat.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ViewDetailDateView, self).get_context_data(*args, **kwargs)
        pk = self.kwargs.get('pk')
        instance = Viewing.objects.get(pk=pk)
        context['s'] = Seat.objects.filter(viewing=instance)
        #context['form'] = BookingForm(initial={'views': instance,'plays':instance.play_name})


        return context



class PlayDetailSlugView(DetailView):
   context_object_name = 'book'
   queryset = Play.objects.all()
   template_name = "plays/detail.html"

   def get_context_data(self, *args, **kwargs):
        context = super(PlayDetailSlugView, self).get_context_data(*args, **kwargs)

        cart_obj = Cart.objects.new_or_get(self.request)
        new_obj = Cart.objects.new_or_get(self.request)

        #pk = self.kwargs['pk']
        #instance = Play.objects.get(pk=pk)
        slug = self.kwargs.get('slug')
        instance = Play.objects.get(slug=slug)
        context['v'] = Viewing.objects.filter(play_name__title=instance)
        context['r'] = Review.objects.filter(play__title=instance).order_by('-id')
        context['cart'] = cart_obj
        return context



#optional try to remove later
   # def get_object(self, *args, **kwargs):
   #     request = self.request
   #     slug = self.kwargs.get('slug')
   #     instance = Play.objects.get(slug=slug)
   #
   #     return instance
