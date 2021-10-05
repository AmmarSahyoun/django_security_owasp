from django.shortcuts import render, redirect
from website.models.timesheet import Timesheet
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def search(request):
    searchText = request.GET.get('searchText')
    if not searchText is None:
        searchTimesheets = Timesheet.objects.filter(notes__contains=searchText)
        return render(request, 'website/searchTimesheet.html', {'searchResults': searchTimesheets, "searchText": searchText})

    return render(request, 'website/searchTimesheet.html')