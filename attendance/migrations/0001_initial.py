# Generated by Django 4.2.3 on 2023-07-26 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0002_staff_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('date_signin', models.DateField(blank=True, null=True)),
                ('time_signin', models.TimeField(blank=True, null=True)),
                ('date_signout', models.DateField(blank=True, null=True)),
                ('time_signout', models.TimeField(blank=True, null=True)),
                ('attendance_day', models.CharField(max_length=20)),
                ('staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
    ]
