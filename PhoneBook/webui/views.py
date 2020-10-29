from django.views import generic
from .models import Phones, Logging
from .forms import PhonesForm
from django.db.models import Q


class PhonesView(generic.ListView):
    model = Phones
    queryset = Phones.objects.all()


class AddPhone(generic.CreateView):
    model = Phones
    form_class = PhonesForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Search(generic.ListView):
    def get_queryset(self):
        return Phones.objects.filter(
            Q(name__icontains=self.request.GET.get("q")) |
            Q(phone__icontains=self.request.GET.get("q"))
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class PhoneDetail(generic.UpdateView):
    model = Phones
    form_class = PhonesForm
    template_name = 'webui/phones_detail.html'
    success_url = "/"

