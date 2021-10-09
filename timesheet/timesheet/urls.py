from django.contrib import admin
from django.urls import path
from website.views import logmein, logmeout, search, home
from website.views.user import myUser, createUser, deleteUser
from website.views.timesheet import timesheet, getTimesheetById, timesheetXml
from website.views.totp import checkTotp

urlpatterns = [
    path('e44002bf-8b73-4827-8a27-f62326e868d0-admin/', admin.site.urls),
    path('login', logmein, name="login"),
    path('home', home, name="home"),
    path('logout', logmeout, name="logout"),
    path('myUser', myUser, name="myUser"),
    path('createUser', createUser, name="createUser"),
    path('deleteUser', deleteUser, name="deleteUser"),
    path('timesheets', timesheet, name="timesheets"),
    path('timesheetsXml', timesheetXml, name="timesheetsXml"),
    path('timesheets/<int:id>', getTimesheetById, name="getTimesheetById"),
    path('timesheets/search', search, name="searchResults"),
    path('login/totpSetup', checkTotp, name="totpSetup"),
]
