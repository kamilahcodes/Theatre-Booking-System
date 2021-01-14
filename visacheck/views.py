from django.shortcuts import render
from .models import Visa
from .forms import VisaForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def visacheck(request,pk=None, *args, **kwargs):
    #selection= None


    if request.method == 'POST':
        form = VisaForm(request.POST)
        if form.is_valid():
             #selection = form.cleaned_data['play']
             pass  # does nothing, just trigger the validation
    else:
        form = VisaForm()

    context ={
    'form':form

    }

    return render(request, "visacheck/visacheck.html", context)


def success(request,pk=None, *args, **kwargs):
    pass

    context ={


    }

    return render(request, "visacheck/success.html", context)
