# Generated by Django 4.1 on 2022-09-15 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0012_remove_inpatient_bill_doctor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inpatient_bill',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospApp.doctor'),
        ),
        migrations.AddField(
            model_name='inpatient_bill',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospApp.room'),
        ),
        migrations.AddField(
            model_name='outpatient_bill',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospApp.doctor'),
        ),
    ]
