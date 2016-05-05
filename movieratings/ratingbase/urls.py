from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rater/(?P<rater_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),

]
