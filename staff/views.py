from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Staff(request):

    if request.method == "POST":
        if models.Staff.objects.filter(pk=request.POST['staffid']).exists():
            messages.error(request, 'Staff Already Exist')
            return redirect('staff')
        else:
            staffid = request.POST['staffid']
            designation = request.POST['designation']
            fullname = request.POST['fullname']
            level = request.POST['level']
            email = request.POST['email']
            phone = request.POST['phone']
            coordinate = request.POST["location"]
            staff = models.Staff.objects.create(staffid=staffid, designation=designation, fullname=fullname,
                                                level=level, email=email, phone=phone, coordinate=coordinate)
            staff.save()
            messages.success(request, 'Staff Added Successfully')
            return redirect('staff')
    return render(request, 'info/addstaff.html')
