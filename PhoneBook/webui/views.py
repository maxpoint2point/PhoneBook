from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from .models import Phones, Logging
from django.views.generic.base import View
from .forms import PhonesForm


class PhonesView(ListView):
    model = Phones
    queryset = Phones.objects.all()


class AddPhone(CreateView):
    model = Phones
    form_class = PhonesForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Search(ListView):
    def get_queryset(self):
        return Phones.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class PhoneDetail(View):
    def get(self, request, pk):
        phone = Phones.objects.get(pk=pk)
        log = Logging.objects.filter(phone=phone)
        return render(request, 'webui/phones_detail.html', {
            'phone': phone,
            'logs': log,
        })
