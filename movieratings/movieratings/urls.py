from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls

urlpatterns = [
    url(r'^ratingbase/', include('ratingbase.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', auth_views.login, {'extra_context': {'next': '/ratingbase/userDetail/5'}}),
    url(r'^', include('django.contrib.auth.urls')),
]
