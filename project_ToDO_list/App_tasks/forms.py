from django import forms
from .models import Detail,Info

class DetailForm(forms.ModelForm):
    class Meta:
        fields =("task_priority","task_code")
        model=Detail

class InfoForm(forms.ModelForm):
    class Meta:
        fields = ("task_name","priority","task_deadline")
        model=Info