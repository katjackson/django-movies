# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 04:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ratingbase', '0020_auto_20160509_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 9, 4, 1, 7, 625190, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
