from django.conf.urls import url
from . import views

app_name = 'ratingbase'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.user_detail, name='userDetail'),
    url(r'^rater/profile/$', views.rater_profile, name='raterProfile'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movieDetail'),
    url(r'^register/', views.register, name='register'),
    url(r'^redirect/', views.redirect, name='redirect'),
    url(r'^edit/(?P<id>[0-9]+)$', views.edit, name='edit'),
]
