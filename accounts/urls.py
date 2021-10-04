from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("api/", include("accounts.api.urls")),
    path("login/", views.indexView, name="authentication"),
]
