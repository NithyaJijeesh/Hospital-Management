# Generated by Django 4.1 on 2022-09-16 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0013_inpatient_bill_doctor_inpatient_bill_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outpatient_bill',
            name='pathology',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospApp.pathology'),
        ),
    ]