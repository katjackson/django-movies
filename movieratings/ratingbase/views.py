from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie, Rater, Rating


def index(request):
    # ratings = Rating.objects.filter(movie=Movie.objects.get(movie_id=6))
    # ratings.aggregate(Avg('rating'))
    return HttpResponse("Hello, world. You're at the ratings database index.")


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    return render(request, 'ratingbase/movie_detail.html', {'movie': movie})


def user_detail(request, rater_id):
    rater = get_object_or_404(Rater, rater_id=rater_id)
    return render(request, 'ratingbase/user_detail.html', {'rater': rater})
