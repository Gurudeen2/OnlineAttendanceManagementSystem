from django.shortcuts import render
from . import models

# Create your views here.

def Staff(request):

    if request.method == "POST":
        staffid = request.POST['staffid']
        designation = request.POST['designation']
        fullname = request.POST['fullname']
        level = request.POST['level']
        email = request.POST['email']
        phone = request.POST['phone']
        staff = models.Staff.objects.create(staffid=staffid, designation=designation, fullname=fullname,
                                            level=level, email=email, phone=phone)
        staff.save()
        return render(request, )
    return render(request, 'info/addstaff.html')
