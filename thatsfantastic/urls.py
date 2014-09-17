from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from thatsfantastic.views import (FilmDetailView, FilmSearchView, FilmListView)

DEBUG = getattr(settings, 'DEBUG', False)

urlpatterns = patterns('',
    url(r'^films/(?P<slug>[\w\-]+)/$', FilmDetailView.as_view(), name='film-detail'),
    url(r'^films/search/$', FilmSearchView.as_view(), name='films-search'),
    url(r'^$', FilmListView.as_view(), name='films-list'),

    url(r'^admin/', include(admin.site.urls)),
)


if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
