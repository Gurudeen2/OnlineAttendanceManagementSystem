from django.db import models
from staff.models import Staff

# Create your models here.

class MarkAttendance(models.Model):

    staffid = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, blank=False, null=False)
    date_signin = models.DateField(blank=True, null=True)
    time_signin = models.TimeField(blank=True, null=True)
    date_signout = models.DateField(blank=True, null=True)
    time_signout = models.TimeField(blank=True, null=True)
    attendance_day = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self) -> str:
        return self.staffid.pk
