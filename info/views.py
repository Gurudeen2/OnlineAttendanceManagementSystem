from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def index(request):
    
    if request.user:
        return render(request, 'info/listattendance.html')
    
    return render(request, 'info/logout.html')


def home(request):

    return render(request, 'info/staff_homepage.html')