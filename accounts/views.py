from django.shortcuts import render
from django.http import HttpResponseRedirect


def indexView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return render(request, "accounts/index.html")
