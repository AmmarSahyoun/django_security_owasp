from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    html = "<h1> Hello from views<H1>"
    return render(request, "mySite/index.html")
    return HttpResponse(html)
