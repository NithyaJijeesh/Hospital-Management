# Generated by Django 4.1 on 2022-09-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0016_remove_inpatient_bill_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inpatient_bill',
            name='misc',
        ),
    ]
