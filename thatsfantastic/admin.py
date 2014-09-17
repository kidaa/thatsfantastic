from django.contrib import admin
from thatsfantastic.models import (Film, Person, Screening)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'runtime', 'year')
    search_fields = ('title', 'long_description')


admin.site.register(Person)
admin.site.register(Screening)
