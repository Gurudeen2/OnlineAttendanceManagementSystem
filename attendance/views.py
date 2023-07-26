from django.shortcuts import render
from staff.models import Staff
from . import models
from datetime import datetime
# Create your views here.

def MarkAttendance(request):
    now = datetime.now()
    if request.method == "POST":
        staffid = request.POST["staffid"]
        date_signin = now.strftime("%d/%m/%Y")
        time_signin = now.strftime("%H:%M:%S")
        attendance_day = now.strftime('%A')

        staff = Staff.objects.get(pk=staffid)
        print("staff", staff)
        if request.POST.get('signin'):
            status="Present"
            date_signout = ""
            time_signout = ""
            attendance = models.MarkAttendance.objects.create(staffid=staff, status=status, date_signin=date_signin,
                                                              time_signin=time_signin, date_signout=date_signout,
                                                              time_signout=time_signout, attendance_day=attendance_day)
            attendance.save()
        if request.POST.get('signout'):
            print("i was signout")
            date_signout = now.strftime("%d/%m/%Y")
            time_signout = now.strftime("%H:%M:%S")
            models.MarkAttendance.objects.filter(staffid=staff).update(date_signout=date_signout,
                                                              time_signout=time_signout)
           
        
    return render(request, 'info/markattendance.html')