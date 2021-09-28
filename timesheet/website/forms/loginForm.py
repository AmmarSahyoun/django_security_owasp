from django.forms import Form, CharField, PasswordInput

class LoginForm(Form):
    username = CharField(max_length=20)
    password = CharField(widget=PasswordInput())
    totp = CharField(max_length=6)

