from django.contrib import admin
from thatsfantastic.models import (Film, Person, Screening)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')


admin.site.register(Person)
admin.site.register(Screening)
