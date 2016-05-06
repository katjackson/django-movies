from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie, Rater, Rating


def index(request):
    significantly_rated = Movie.objects.filter(ratings_count__gte=15)
    top_twenty = significantly_rated.order_by('avg_rating').reverse()[:20]
    return render(request, 'ratingbase/index.html', {'top_twenty': top_twenty})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    movie_ratings = Rating.objects.filter(movie=movie)
    return render(request, 'ratingbase/movie_detail.html', {'movie': movie, 'movie_ratings': movie_ratings})


def user_detail(request, rater_id):
    rater = get_object_or_404(Rater, rater_id=rater_id)
    ratings = Rating.objects.filter(rater=rater)
    return render(request, 'ratingbase/user_detail.html', {'rater': rater, 'ratings': ratings})
