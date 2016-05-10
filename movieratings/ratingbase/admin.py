from django.contrib import admin
from .models import Rating, Movie, Rater


class RatingAdmin(admin.ModelAdmin):
    fields = ['rater', 'rating']
    list_display = ('movie', 'rating', 'rater', 'id')

admin.site.register(Rating, RatingAdmin)


class RatingInline(admin.StackedInline):
    model = Rating


class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'genre']
    inlines = [RatingInline]

admin.site.register(Movie, MovieAdmin)


class RaterAdmin(admin.ModelAdmin):
    fields = ['age', 'gender', 'occupation', 'zip_code']
    list_display = ('rater_id', 'age')

admin.site.register(Rater, RaterAdmin)
