from django.urls import path
from . import views

urlpatterns = [
    path("", views.PhonesView.as_view()),
    path("add", views.AddPhone.as_view(), name="add_phone"),
    path("search/", views.Search.as_view(), name="search"),
    path('phone/<int:pk>/', views.PhoneDetail.as_view(), name="detail"),
]
