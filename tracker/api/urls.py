from django.urls import path
from .views import UrlListView, UrlDetailView

app_name = "api"

urlpatterns = [
    path("list-url/", UrlListView.as_view(), name="list_url"),
    path(
        "detail-url/<int:url_id>/",
        UrlDetailView.as_view(),
        name="detail_url",
    ),
]
