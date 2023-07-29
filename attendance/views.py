from django.shortcuts import render, redirect
from staff.models import Staff
from . import models
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            if not models.MarkAttendance.objects.filter(staffid=staff).filter(date_signin=date_signin).exists():
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
            date_signout = now.strftime("%Y-%m-%d")
            time_signout = now.strftime("%H:%M:%S")
            if  not models.MarkAttendance.objects.filter(staffid=staff).filter(
                date_signin=date_signin).filter(attendance_day=attendance_day).filter(date_signout=date_signout).exists():
                print("cond")
                models.MarkAttendance.objects.filter(staffid=staff).filter(
                    attendance_day=attendance_day).filter(
                date_signin=date_signin).update(date_signout=date_signout,time_signout=time_signout)
                messages.success(request, 'You Signed Out')
                return redirect('markattend')
            else:
                messages.error(request, 'You"ve Signout Already')
                return redirect('markattend')

            
        
    return render(request, 'info/markattendance.html')

def IndividualAttendance(request, param):
    print("parameter", param)
    single_view = models.MarkAttendance.objects.filter(staffid=param)
    fullname = single_view.first().staffid.fullname
    staffid = param
    absent_count = single_view.filter(status="Absent").count()
    present_count = single_view.filter(status="Present").count()
    lastattendance= single_view.latest('date_signout').date_signin
    return render(request, 'info/individualattendance.html', {'fullname':fullname, 'staffid':staffid,
                                                               'absentcount':absent_count,
                                                                'presentcount':present_count,
                                                                'lastattendance':lastattendance })

def ListAttendance(request):
    attendance = models.MarkAttendance.objects.all()
    searchparam = request.GET.get('search')
    page = request.GET.get('page', 1)

    
    if searchparam:
        attendance = models.MarkAttendance.objects.filter(Q(staffid=searchparam)|Q(status=searchparam))

    paginator = Paginator(attendance, 15)
    try:
        attendance = paginator.page(page)
    except PageNotAnInteger:
        attendance = paginator.page(1)
    except EmptyPage:
        attendance = paginator.page(paginator.num_pages)
    

    return render(request, 'info/listattendance.html', {"allattendance":attendance})