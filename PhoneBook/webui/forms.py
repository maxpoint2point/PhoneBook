from django import forms
from .models import Phones


class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ("name", "phone", "manager",)
