from django import forms
from .models import Phones


class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ("name", "phone", "manager",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "manager": forms.TextInput(attrs={"class": "form-control"}),
        }
