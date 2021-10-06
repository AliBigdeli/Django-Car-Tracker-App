from django.urls import path, include
from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.indexView, name="index"),
    path("device/list", views.deviceListView, name="device_list"),
    path("device/<str:token>", views.deviceDetailView, name="device_detail"),
    path("api/", include("tracker.api.urls")),
]
