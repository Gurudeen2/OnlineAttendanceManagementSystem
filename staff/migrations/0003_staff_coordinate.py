# Generated by Django 4.2.3 on 2023-12-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='coordinate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]