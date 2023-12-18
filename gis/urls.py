from django.urls import path

from . import views

urlpatterns = [
    path("gisx", views.gisx, name="gisx"),
]