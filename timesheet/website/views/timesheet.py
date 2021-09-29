from django.shortcuts import render, HttpResponse
from website.forms.timesheetForm import TimesheetForm
from website.forms.timesheetXmlForm import TimesheetXmlForm
from website.models.timesheet import Timesheet
from datetime import date, datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from lxml import etree
from django.utils.dateparse import parse_date

@login_required(login_url="/login")
def getTimesheetById(request, id):
    timesheet = Timesheet.objects.get(id=id)
    form = TimesheetForm(initial=timesheet.__dict__)
    return render(request, "website/timesheet.html", {"form": form})

@csrf_exempt
@login_required(login_url="/login")
def timesheet(request):
    if request.method == "POST":
        return postTimesheet(request)

    now = datetime.now()
    form = TimesheetForm(initial=
        {
            "userId":request.user.id, 
            "approved": False, 
            "date": date.today(),
            "timeFrom": (now + timedelta(hours=-1)).strftime("%H:%M"),
            "timeTo": now.strftime("%H:%M"),
            "totalMinutes": 0
        })
    return render(request, "website/timesheet.html", {"form": form})

@login_required(login_url="/login")
def postTimesheet(request):
    form = TimesheetForm(request.POST)
    if form.is_valid():
        if allowApprove(request):
            form.save()
        else:
            timesheet = form.save(commit=False)
            timesheet.approved = False
            timesheet.save()

    return render(request, "website/timesheet.html", {"form": form})

@login_required(login_url="/login")
def timesheetXml(request):
    if request.method == "POST":
        return postTimesheetXML(request)

    now = datetime.now()
    form = TimesheetXmlForm()
    return render(request, "website/timesheetXml.html", {"form": form})

@login_required(login_url="/login")
def postTimesheetXML(request):
    root = ""
    if request.method=="POST":
        data = request.POST["xmlData"]
        parser = etree.XMLParser(resolve_entities=False)
        root = etree.fromstring(data, parser=parser)

        timesheet = Timesheet()
        timesheet.date = parse_date(root.find("date").text)
        timesheet.timeFrom = root.find("timeFrom").text
        timesheet.timeTo = root.find("timeTo").text
        timesheet.notes = root.find("notes").text
        timesheet.userId = root.find("userId").text
        timesheet.totalMinutes = root.find("totalMinutes").text
        timesheet.approved = False
        timesheet.save()

    return HttpResponse(etree.tostring(root))

def allowApprove(request):     
    if request.user.has_perm("website.approve_timesheet"):
        return True
    else:
        return False