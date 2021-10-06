from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Device

@login_required
def indexView(request):
    return render(request, "tracker/index.html")

@login_required
def deviceListView(request):
    return render(request, "tracker/device_list.html")

@login_required
def deviceDetailView(request,token):
    device = Device.objects.get(token=token)
    context = {"device":device}
    return render(request, "tracker/device_detail.html",context)
