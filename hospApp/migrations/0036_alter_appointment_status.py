# Generated by Django 4.1 on 2022-09-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0035_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=False, null=True),
        ),
    ]