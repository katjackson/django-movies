# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 22:10
from __future__ import unicode_literals
from django.db import migrations, models
import pandas as pd


def initialize_rating_data(apps, schema_editor):
    Movie = apps.get_model('ratingbase', 'Movie')
    Rater = apps.get_model('ratingbase', 'Rater')
    Rating = apps.get_model('ratingbase', 'Rating')

    rating = pd.read_csv(
        '/Users/Oakes/Desktop/data/ratings.dat',
        sep='::', names=['rater_id', 'movie_id', 'rating', 'timestamp'],
        header=None)

    for row in rating.iterrows():
        row = row[1].to_dict()
        new = Rating(rater=Rater.objects.get(rater_id=row['rater_id']),
                     movie=Movie.objects.get(movie_id=row['movie_id']),
                     rating=row['rating'])
        new.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ratingbase', '0009_auto_20160504_2226'),
    ]

    operations = [
        migrations.RunPython(initialize_rating_data),
    ]
