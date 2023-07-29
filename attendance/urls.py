from django.urls import path
from . import views

urlpatterns =[
    path('', views.MarkAttendance, name='markattend'),
    path('all/', views.ListAttendance, name='listattendance'),
    path('staffattendance/<slug:param>', views.IndividualAttendance, name='staffattendance')

]