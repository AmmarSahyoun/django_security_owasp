from django import forms
from django.forms import Form, CharField, PasswordInput
from django.contrib.auth.password_validation import validate_password

class CreateUserForm(forms.Form):
    username = CharField(max_length=30)
    email = CharField(max_length=50)
    password = CharField(widget=PasswordInput())

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password