from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ratingbase/', include('ratingbase.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
]
