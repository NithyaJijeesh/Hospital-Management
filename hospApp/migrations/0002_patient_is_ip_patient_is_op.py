# Generated by Django 4.1 on 2022-09-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_ip',
            field=models.BooleanField(default=False, verbose_name='ip status'),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_op',
            field=models.BooleanField(default=False, verbose_name='op status'),
        ),
    ]