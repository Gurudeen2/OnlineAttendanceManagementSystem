from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='index'),
    path('staffadmin/', views.index, name='staffadmin'),
   

]