from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def anon(request):
    return render(request, 'website/anon.html')
