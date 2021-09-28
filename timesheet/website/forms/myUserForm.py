from django.forms import ModelForm, TextInput, HiddenInput
from website.models import UserDetails 

class MyUserForm(ModelForm):
    class Meta:
        model = UserDetails 
        fields = ('userId', 'phone', 'routingNumber', 'accountNumber')
        widgets = {
            'userId': HiddenInput(),
            'phone': TextInput(),
            'routingNumber': TextInput(),
            'accountNumber': TextInput(),
        }
