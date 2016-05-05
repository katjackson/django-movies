from django.contrib import admin
from .models import Rating, Movie, Rater

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
