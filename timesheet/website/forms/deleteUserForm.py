from django import forms
from django.forms import CharField

class DeleteUserForm(forms.Form):
    username = CharField(max_length=30)