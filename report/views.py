from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from attendance import models

# Create your views here.

def Reportall(request):
    report = models.MarkAttendance.objects.all()
    searchparam = request.GET.get('search')
    page = request.GET.get('page', 1)

    print("aa",a)
    
    if searchparam:
        report = models.MarkAttendance.objects.filter(Q(staffid=searchparam)|Q(status=searchparam))

    paginator = Paginator(report.order_by("staffid"), 15)
    try:
        report = paginator.page(page)
    except PageNotAnInteger:
        report = paginator.page(1)
    except EmptyPage:
        report = paginator.page(paginator.num_pages)
    
    datefrom = request.GET.get('fromdate')
    dateto = request.GET.get('todate')
    print("dateto", dateto)
    # if datefrom and dateto:
    #     report = models.MarkAttendance.objects.filter(date_signin__range=["2023-07-25", "2023-07-26"])

    return render(request, 'info/report.html', {"allreport":report})