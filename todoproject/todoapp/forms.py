
from .models import mod
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model = mod
        fields = ['item','priority','date']