from django.db import models
from staff.models import Staff

# Create your models here.

class MarkAttendance(models.Model):

    staffid = models.ForeignKey(Staff, on_delete=models.CASCADE)
    attendance
    date_signin
    time_signin
    date_signout
    time_signout
    attendance_day
