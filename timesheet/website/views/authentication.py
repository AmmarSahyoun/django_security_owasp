from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from website.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from website.views.totp import validateTotp
from website.models.logEntry import LogEntry
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
@login_required(login_url='/login')
def logmeout(request):
    logout(request)
    return redirect('/login')

@csrf_exempt
def logmein(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            totp = request.POST['totp']
            user = authenticate(username=username, password=password, request=request)
            if user is not None:
                if validateTotp(request, user.id, totp):
                    login(request, user)
                    return redirect("/home")
                else:
                    ip = request.META.get('REMOTE_ADDR')
                    logger.warning(LogEntry(action='on_login_fail_totp', ipAddress=ip, user=username))
                    return HttpResponse("Incorrect TOTP")
            else:
                ip = request.META.get('REMOTE_ADDR')
                logger.warning(LogEntry(action='on_login_fail', ipAddress=ip, user=username))
                return HttpResponse("login failed")
    else:
        form = LoginForm()
    
    return render(request, "website/login.html", {"form": form})