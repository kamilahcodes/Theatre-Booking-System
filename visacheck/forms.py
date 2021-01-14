from django import forms

from .models import Visa



class VisaForm(forms.Form):
    card_holder = forms.CharField(max_length=120)
    cc_no = forms.IntegerField()
    expiry_date= forms.IntegerField()
    csv=forms.IntegerField()
