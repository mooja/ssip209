from django.core.urlresolvers import reverse
from django.db import models
from autoslug import AutoSlugField
from swingtime.models import Event, Occurrence


class SSIPEvent(Event):
    details = models.TextField(null=True, blank=True)
    default_location = models.ForeignKey('Location', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Actual Event"
        verbose_name_plural = "Actual Events"


class SSIPOccurrence(Occurrence):
    location = models.ForeignKey('Location', null=True)
    organizer = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('events:ssipoccurrence-detail',
                       args=[str(self.id), str(self.event.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Actual Occurrence"
        verbose_name_plural = "Actual Occurrences"


class Location(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    address = models.CharField(max_length=400, null=True)
    description = models.TextField()
    maphtml = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('events:location-detail',
                           args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
