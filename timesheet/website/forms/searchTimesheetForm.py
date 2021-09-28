from django.forms import Form, CharField

class SearchTimesheetForm(Form):
    searchText = CharField(max_length=30)
