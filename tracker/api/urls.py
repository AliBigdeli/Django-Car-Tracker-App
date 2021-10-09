from django.urls import path
from .views import DeviceListView, DeviceDetailView, CoordinateListView, CoordinateCurrentView,CoordinateGetView

app_name = "api"

urlpatterns = [
    path("device/list", DeviceListView.as_view(), name="list_device"),
    path("device/<str:token>",
         DeviceDetailView.as_view(), name="detail_device"),
    path("device/<str:token>/coordinate",
         CoordinateListView.as_view(), name="list_coordinate"),
     path("device/<str:token>/coordinate/get",
         CoordinateGetView.as_view(), name="get_data_coordinate"),
    path("device/<str:token>/coordinate/current",
         CoordinateCurrentView.as_view(), name="current_coordinate")

]
