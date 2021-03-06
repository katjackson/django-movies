# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=90)),
                ('genre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('rater_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('Q', 'Genderqueer')], max_length=2)),
                ('age', models.IntegerField(blank=True, choices=[(1, 'Under 18'), (18, '18-24'), (25, '25-34'), (35, '35-44'), (45, '45-49'), (50, '50-55'), (56, '56+')])),
                ('occupation', models.IntegerField(blank=True, choices=[(0, 'Other'), (1, 'Academic/Educator'), (2, 'Artist'), (3, 'Clerical/Admin'), (4, 'College/Grad Student'), (5, 'Customer Service'), (6, 'Doctor/Health Care'), (7, 'Executive/Managerial'), (8, 'Farmer'), (9, 'Homemaker'), (10, 'K-12 Student'), (11, 'Lawyer'), (12, 'Programmer'), (13, 'Retired'), (14, 'Sales/Marketing'), (15, 'Scientist'), (16, 'Self-employed'), (17, 'Technician/Engineer'), (18, 'Tradesman/Craftsman'), (19, 'Unemployed'), (20, 'Writer')])),
                ('zip_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingbase.Movie')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingbase.Rater')),
            ],
        ),
    ]
