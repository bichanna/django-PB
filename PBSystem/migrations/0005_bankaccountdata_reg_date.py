# Generated by Django 3.0.2 on 2021-01-26 01:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PBSystem', '0004_auto_20210121_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccountdata',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]