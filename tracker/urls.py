from django.urls import path, include
from . import views

appname = "tracker"

urlpatterns = [
    path("", views.indexView, name="index"),
    path("api/", include("tracker.api.urls")),
]
