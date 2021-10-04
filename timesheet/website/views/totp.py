from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from website.models.totp import Totp
from io import BytesIO
import pyotp
import base64
import qrcode

@login_required(login_url='/login')
def checkTotp(request):
    if request.method == "POST":
        totp = request.POST['totp']
        if validateTotp(request, request.user.id, totp):
            return redirect("/home")
        else:
            return HttpResponse("Wrong TOTP")

def validateTotp(request, userId, submittedTotp):
    userTotpRecord = Totp.objects.get(userId=userId)
    totp = pyotp.TOTP(userTotpRecord.secret)
    currentTotp = totp.now()
    if submittedTotp == currentTotp:    
        request.session['MfaAccepted'] = True
    else:
        request.session['MfaAccepted'] = False

    return request.session['MfaAccepted']

def totpBase64Image(secret, email):
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name='TimesheetApp')
    img = qrcode.make(uri)
    output_buffer = BytesIO()
    img.save(output_buffer, format='PNG')
    binary_data = output_buffer.getvalue()
    base64_data = base64.b64encode(binary_data)
    return 'data:image/png;base64,' + base64_data.decode()

def newTotp(user):
    secret = pyotp.random_base32()
    totp = Totp(userId=user.id, secret=secret)
    totp.save()
    return totp