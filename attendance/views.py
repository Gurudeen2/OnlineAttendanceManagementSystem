from django.shortcuts import render, redirect
from staff.models import Staff
from . import models
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import math


def distance(lat1, lon1, lat2, lon2):
    r = 6371
    p = math.pi/180
    a = 0.5 - math.cos((lat2-lat1)*p)/2 + math.cos(lat1*p) * math.cos(lat2*p)*(1-math.cos((lon2-lon1)*p))/2
    return 2*r* math.asin(math.sqrt(a)) 
# Create your views here.
# @login_required
def MarkAttendance(request):
      
    # ['7.7326 4.4256']
    now = datetime.now()
    if request.method == "POST":
        staffid = request.POST["staffid"]
        date_signin = now.strftime("%Y-%m-%d")
        time_signin = now.strftime("%H:%M:%S")
        attendance_day = now.strftime('%A')
        location = request.POST["loc"]
        print("location", location)
       
        
        
        if request.POST.get('signin'):
            
            #staffid n date to filter
            if Staff.objects.filter(pk=staffid) and location:
                staff = Staff.objects.get(pk=staffid)
               
                coordinate = staff.coordinate
                coordinate = coordinate.split(" ")
                mygps = location.split(" ")
                
               
                latitude = coordinate[0].replace(",","")
                longtitude = coordinate[1].replace(",","")
                mylatitude = mygps[0].replace(",","")
                mylongtitude = mygps[1].replace(",","")
                
               
                dis = distance(float(mylongtitude), float(longtitude), float(mylatitude), float(latitude))
                
              

                if dis >= 0 and dis <=2:

                        
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
                else:
                    messages.error(request, 'You can not mark attendance, You are not in the School Location')
                    return redirect('markattend')

            else:
                messages.error(request, 'Invalid Staff ID ')
                return redirect('markattend')

        if request.POST.get('signout'):
            now_UTC = datetime.utcnow()
            if( now_UTC.hour + 1 > 15):
                
                date_signout = now.strftime("%Y-%m-%d")
                time_signout = now.strftime("%H:%M:%S")

                if Staff.objects.filter(pk=staffid):
                    staff = Staff.objects.get(pk=staffid)
                    if  not models.MarkAttendance.objects.filter(staffid=staff).filter(
                        date_signin=date_signin).filter(attendance_day=attendance_day).filter(date_signout=date_signout).exists():
                        models.MarkAttendance.objects.filter(staffid=staff).filter(
                            attendance_day=attendance_day).filter(
                        date_signin=date_signin).update(date_signout=date_signout,time_signout=time_signout)
                        messages.success(request, 'You Signed Out')
                        return redirect('markattend')
                    else:
                        messages.error(request, 'You"ve Signout Already')
                        return redirect('markattend')
                else:
                    messages.error(request, 'Invalid Staff ID')
                    return redirect('markattend')
                
            else:
                messages.error(request, 'You Can"t Signout Yet, is not 4pm Yet')
                return redirect('markattend')
            
        
    return render(request, 'info/markattendance.html')

@login_required
def IndividualAttendance(request, param):
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

@login_required
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