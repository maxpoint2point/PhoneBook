from django import forms
from .models import Phones
from django.contrib.auth.models import User


class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ("name", "phone", "manager",)
        manager = forms.ModelChoiceField(queryset=User.objects.all())
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            # "manager": forms.ChoiceField(attrs={"class": "form-control"}),
        }
