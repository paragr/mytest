# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessreq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrequests',
            name='message',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
