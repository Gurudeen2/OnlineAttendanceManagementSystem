from django.shortcuts import render
from staff.models import Staff
from . import models
from datetime import datetime
# Create your views here.

def Signin(request):
    now = datetime.now()
    if request.method == "POST":
        staffid = request.POST["staffid"]
        status = "Present"
        date_signin = now.strftime("%d/%m/%Y")
        time_signin = now.strftime("%H:%M:%S")
        date_signout = ""
        time_signout = ""
        attendance_day = now.strftime('%A')

        staff = Staff.objects.get(pk=staffid)
        attendance = models.MarkAttendance.objects.create(staffid=staff, )
    return render(request, 'info/markattendance.html')