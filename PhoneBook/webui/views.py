from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Phones
from django.views.generic.base import View
from .forms import PhonesForm


class PhonesView(ListView):
    model = Phones
    queryset = Phones.objects.all()


class AddPhone(View):
    def post(self, request):
        form = PhonesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    def get(self, request):
        return render(request, 'webui/create.html')

