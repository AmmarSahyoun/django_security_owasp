from django.contrib.auth.models import User, Group
from django.shortcuts import render, HttpResponse
from website.forms.myUserForm import MyUserForm
from website.forms.createUserForm import CreateUserForm
from website.forms.deleteUserForm import DeleteUserForm
from website.models.userDetails import UserDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from website.views.totp import newTotp, totpBase64Image
from website.decorators import logged_permission_required

@login_required(login_url="/login")
def myUser(request):
    currentUser = UserDetails.objects.get(userId=request.user.id)
    if request.method == "POST":
        form = MyUserForm(request.POST, instance=currentUser)
        if form.is_valid():
            form.save()
    else:
        form = MyUserForm(initial=vars(currentUser))

    return render(request, "website/myUser.html", {"form": form})

@logged_permission_required(permission="auth.delete_user")
def deleteUser(request):
    if request.method == "POST":
        form = DeleteUserForm(request.POST)
        try:
            username = request.POST['username']
            userRecord = User.objects.get(username=username)
            userRecord.delete()
            return render(request, "website/message.html", {"message": "User deleted"})
        except Exception as e:
            return render(request, "website/deleteUser.html", {"message": str(e), "form": form})
    else:
        form = DeleteUserForm()

    return render(request, "website/deleteUser.html", {"form": form})

def createUser(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            user = User.objects.create_user(username, email, password) 
            addToGroup(user, "TimesheetUsers") 
            userDetails = UserDetails(userId=user.id, hourlyRate=5, phone="", routingNumber = "", accountNumber="")
            userDetails.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            totp = newTotp(user)
            base64Image = totpBase64Image(totp.secret, email)
            return render(request, "website/totpSetup.html", {"base64Image": base64Image})
    else:
        form = CreateUserForm()

    return render(request, "website/createUser.html", {"form": form})

def addToGroup(user, groupName):
    timesheetUsersGroup = Group.objects.get(name=groupName) 
    user.groups.add(timesheetUsersGroup)
