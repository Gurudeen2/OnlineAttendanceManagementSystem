from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def index(request):
    
    if request.user:
        print("user", request.user)
        return render(request, 'info/staff_homepage.html')
    
    return render(request, 'info/logout.html')
