# Generated by Django 4.1 on 2022-09-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0023_inpatient_bill_total'),
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
        migrations.RemoveField(
            model_name='outpatient_bill',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='outpatient_bill',
            name='pathology',
        ),
        migrations.AddField(
            model_name='outpatient_bill',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
