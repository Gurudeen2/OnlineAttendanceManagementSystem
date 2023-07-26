from django.shortcuts import render, redirect
from staff.models import Staff
from . import models
from datetime import datetime
from django.contrib import messages

# Create your views here.

def MarkAttendance(request):
    now = datetime.now()
    if request.method == "POST":
        staffid = request.POST["staffid"]
        date_signin = now.strftime("%Y-%m-%d")
        time_signin = now.strftime("%H:%M:%S")
        attendance_day = now.strftime('%A')

        staff = Staff.objects.get(pk=staffid)
        if request.POST.get('signin'):
            #staffid n date to filter
            if not models.MarkAttendance.objects.filter(staffid=staff).exists() and models.MarkAttendance.objects.filter(staffid=staff).exists() :
                status="Present"
                attendance = models.MarkAttendance.objects.create(staffid=staff, status=status, date_signin=date_signin,
                                                              time_signin=time_signin,  attendance_day=attendance_day)
                attendance.save()
                messages.success(request, "Attendance Marked!!!")
                return redirect('markattend')
            else:
                messages.error(request, 'Attendance Already Been Marked!!')
                return redirect('markattend')
            
        if request.POST.get('signout'):
            print("i was signout")
            date_signout = now.strftime("%Y-%m-%d")
            time_signout = now.strftime("%H:%M:%S")
            models.MarkAttendance.objects.filter(staffid=staff).update(date_signout=date_signout,
                                                              time_signout=time_signout)
           
        
    return render(request, 'info/markattendance.html')