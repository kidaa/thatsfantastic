from django.conf.urls import patterns, include, url
from django.contrib import admin
from thatsfantastic.views import FilmDetailView


urlpatterns = patterns('',
    url(r'^films/(?P<pk>\d+)/$', FilmDetailView.as_view(), name='film-detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
