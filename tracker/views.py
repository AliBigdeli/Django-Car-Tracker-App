from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def indexView(request):
    return render(request, "tracker/index.html")
