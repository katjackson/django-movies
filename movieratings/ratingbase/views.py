from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import RaterForm, RatingForm
from django.contrib.auth import authenticate, login, views
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Movie, Rater, Rating


def index(request):
    significantly_rated = Movie.objects.filter(ratings_count__gte=15)
    top_twenty = significantly_rated.order_by('avg_rating').reverse()[:20]
    return render(request, 'ratingbase/index.html', {'top_twenty': top_twenty})


def movie_detail(request, movie_id):
    context = {}

    movie = get_object_or_404(Movie, movie_id=movie_id)
    context['movie'] = movie

    movie_ratings = Rating.objects.filter(movie=movie)
    context['movie_ratings'] = movie_ratings

    rating_form = RatingForm()
    context['rating_form'] = rating_form

    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.movie = movie
            new_rating.rater = request.user.rater
            new_rating.save()
            return HttpResponseRedirect('/ratingbase/')
        else:
            print(rating_form.errors)

    else:
        return render(request, 'ratingbase/movie_detail.html', context)


def user_detail(request, rater_id):
    rater = get_object_or_404(Rater, rater_id=rater_id)
    ratings = Rating.objects.filter(rater=rater)
    return render(request, 'ratingbase/user_detail.html', {'rater': rater, 'ratings': ratings})


@login_required
def redirect(request):
    url = '/ratingbase/rater/{}/'.format(request.user.rater.rater_id)
    return HttpResponseRedirect(url)


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        rater_form = RaterForm(request.POST)
        if user_form.is_valid() and rater_form.is_valid():
            new_user = user_form.save()
            new_rater = rater_form.save(commit=False)
            new_rater.user = new_user
            new_rater.save()
            return HttpResponseRedirect("/ratingbase/")
        else:
            print(user_form.errors, rater_form.errors)
    else:
        user_form = UserCreationForm()
        rater_form = RaterForm()
    return render(request, "registration/register.html", {
        'user_form': user_form,
        'rater_form': rater_form,
    })
