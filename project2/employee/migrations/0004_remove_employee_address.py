# Generated by Django 2.0.6 on 2018-06-14 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
    ]
