# Generated by Django 4.1 on 2022-09-16 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0015_remove_outpatient_bill_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inpatient_bill',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='inpatient_bill',
            name='pathology',
        ),
        migrations.RemoveField(
            model_name='inpatient_bill',
            name='room',
        ),
    ]