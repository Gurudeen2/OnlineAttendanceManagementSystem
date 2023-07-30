from django.urls import path
from . import views
from attendance.views import IndividualAttendance

urlpatterns=[
    path('', views.Reportall, name='report'),
    path('invoice/', views.GeneratePdf.as_view(), name='invoice'),
    path('single/<slug:param>', IndividualAttendance, name='singlereport')

]