# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enviornments', '0002_auto_20170923_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enviornments',
            options={'permissions': (('can_stop_services', 'Stop Enviornment Services'), ('can_start_services', 'Start Enviornment Services'), ('can_view_services', 'View Enviornment Services'))},
        ),
    ]
