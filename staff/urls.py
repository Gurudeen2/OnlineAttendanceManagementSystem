from django.urls import path
from . import views


urlpatterns =[
    path('', views.Staff, name="staff")
]