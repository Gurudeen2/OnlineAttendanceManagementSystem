from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from attendance import models
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf #created in step 4

# Create your views here.

def Reportall(request):
    report = models.MarkAttendance.objects.all()
    searchparam = request.GET.get('search')
    page = request.GET.get('page', 1)

    
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
    if datefrom and dateto:
        report = models.MarkAttendance.objects.filter(date_signin__range=["2023-07-25", "2023-07-26"])

    return render(request, 'info/report.html', {"allreport":report})



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('info/invoice.html')
        data = {
             'today': datetime.now(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        html = template.render({"data":data})
        pdf = render_to_pdf('info/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')