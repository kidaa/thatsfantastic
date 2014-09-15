from django.db import models
from django.utils.translation import ugettext as _
from djorm_pgarray.fields import TextArrayField
from django_countries import countries

COUNTRY_CODES = tuple(countries)


def default_list():
    return []


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(blank=True, max_length=50, default='')
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __unicode__(self):
        return '{first} {middle} {last}'.format(first=self.first_name,
                                                middle=self.middle_name,
                                                last=self.last_name)


class Film(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    country = TextArrayField(choices=COUNTRY_CODES, default=default_list)
    language = TextArrayField(default=default_list)
    year = models.PositiveIntegerField(blank=True, null=True, help_text=_("Release year"))
    runtime = models.IntegerField(blank=True, null=True, help_text=_("Film runtime, in whole minutes"))
    directors = models.ManyToManyField('Person', related_name='directed', blank=True, null=True,
                                       help_text=_("Usually one person, but can accomodate multiple directors"))
    actors = models.ManyToManyField('Person', related_name='acted_in', blank=True, null=True)

    class Meta:
        verbose_name = _('Film')
        verbose_name_plural = _('Films')

    def __unicode__(self):
        return '{title} [{year}]'.format(title=self.title, year=self.year)


class Screening(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    film = models.ForeignKey('Film')
    location = models.CharField(blank=True, default='', max_length=120,
                                help_text=_("Location of film screening"))

    class Meta:
        verbose_name = _('Screening')
        verbose_name_plural = _('Screenings')

    def __unicode__(self):
        pass