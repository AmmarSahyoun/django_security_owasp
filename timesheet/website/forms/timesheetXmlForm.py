from django.forms import Form, CharField, Textarea

class TimesheetXmlForm(Form):
    xmlData = CharField(widget=Textarea(attrs={'cols': 77, 'rows': 15}), max_length=4096)
