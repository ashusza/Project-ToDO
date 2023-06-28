from django import forms
from .models import Detail,Info

class DetailForm(forms.ModelForm):
    class Meta:
        fields =("__all__")
        model=Detail

class InfoForm(forms.ModelForm):
    class Meta:
        fields = ("__all__")
        model=Info