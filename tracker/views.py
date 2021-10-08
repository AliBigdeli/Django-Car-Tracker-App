from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Device
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



@login_required
def indexView(request):
    return render(request, "tracker/index.html")

@login_required
def deviceListView(request):
    return render(request, "tracker/device_list.html")

@login_required
def deviceDetailView(request,token):
    auth_token = Token.objects.get(user=request.user)
    device = Device.objects.get(token=token)
    context = {"device":device,"api_key":auth_token}
    return render(request, "tracker/device_detail.html",context)
