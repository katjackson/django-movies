# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingbase', '0021_rating_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
