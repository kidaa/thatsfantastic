from django.views.generic.detail import DetailView
from thatsfantastic.models import Film


class FilmDetailView(DetailView):
    model = Film
