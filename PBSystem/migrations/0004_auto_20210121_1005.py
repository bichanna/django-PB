# Generated by Django 3.0.2 on 2021-01-21 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PBSystem', '0003_auto_20210121_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccountdata',
            name='match',
        ),
        migrations.RemoveField(
            model_name='bankaccountdata',
            name='wether_complete',
        ),
    ]