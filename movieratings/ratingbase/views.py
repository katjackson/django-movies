from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie, Rater, Rating


def index(request):
    top_twenty = Movie.objects.order_by('avg_rating').reverse()[:20]
    return render(request, 'ratingbase/index.html', {'top_twenty': top_twenty})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    return render(request, 'ratingbase/movie_detail.html', {'movie': movie})


def user_detail(request, rater_id):
    rater = get_object_or_404(Rater, rater_id=rater_id)
    return render(request, 'ratingbase/user_detail.html', {'rater': rater})
