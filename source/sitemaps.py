from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

from views import upcoming_events_query
from news.models import NewsEntry


class NewsSitemap(Sitemap):

    def items(self):
        return NewsEntry.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

    def location(self, obj):
        return reverse('home')


class EventsSitemap(Sitemap):
    def items(self):
        return upcoming_events_query()

    def location(self, obj):
        return reverse('events:occurrence-detail',
                       args=(obj.event.id, obj.id))


class StaticSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return ['about', 'home']

    def location(self, item):
        return reverse(item)
