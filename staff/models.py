from django.db import models

# Create your models here.

class Staff(models.Model):
    staffid = models.CharField(primary_key=True, max_length=50, blank=False, null=False)
    fullname = models.CharField(max_length=70, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.staffid