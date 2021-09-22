from django.db import models

class Timesheet(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    userId = models.IntegerField()
    date = models.DateField()
    timeFrom = models.TimeField()
    timeTo = models.TimeField()
    totalMinutes = models.IntegerField()
    approved = models.BooleanField(default=False)
    notes = models.CharField(max_length=200)
