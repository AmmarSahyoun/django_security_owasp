from django.forms import ModelForm, TextInput, HiddenInput, DateInput, TimeInput, CheckboxInput
from website.models.timesheet import Timesheet 

class TimesheetForm(ModelForm):
    class Meta:
        model = Timesheet 
        fields = ['date', 'userId', 'timeFrom', 'timeTo', 'notes', 'totalMinutes', 'approved']
        widgets = {
            'userId': HiddenInput(),
            'date': DateInput(attrs={"type":"date"}),
            'timeFrom': TimeInput(attrs={'type': 'time'}),
            'timeTo': TimeInput(attrs={'type': 'time'}),
            "notes": TextInput(attrs={'size':100, 'maxlength':200}),
            'totalMinutes': HiddenInput(),
        }
