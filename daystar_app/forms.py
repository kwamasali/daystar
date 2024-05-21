from django import forms
from .models import *

class BabyForm(forms.ModelForm): 
    class Meta:
        model = Babies
        fields = '__all__'

class SittersForm(forms.ModelForm): 
    class Meta:
        model = Sitter
        fields = '__all__'

class DollsForm(forms.ModelForm): 
    class Meta:
        model = DollsShop
        fields = '__all__'

class PaymentForm(forms.ModelForm): 
    class Meta:
        model = Payment
        fields = '__all__'

class CheckinForm(forms.ModelForm): 
    class Meta:
        model = CheckIn
        fields = '__all__'