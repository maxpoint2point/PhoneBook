from django.urls import path
from . import views

urlpatterns = [
    path("", views.PhonesView.as_view()),
    path("add/", views.AddPhone.as_view(), name="add_phone"),
]
