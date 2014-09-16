from django.conf.urls import patterns, include, url
from django.contrib import admin
from thatsfantastic.views import FilmDetailView, FilmSearchView


urlpatterns = patterns('',
    url(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name='film-detail'),
    url(r'^films/search/$', FilmSearchView.as_view(), name='films-search'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
