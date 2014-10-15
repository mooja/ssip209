# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from views import HomeView
from sitemaps import StaticSitemap, NewsSitemap, EventsSitemap

from django.contrib import admin
admin.autodiscover()

sitemaps = {'static': StaticSitemap,
            'news': NewsSitemap,
            'events': EventsSitemap}

urlpatterns = patterns('',
    url(r'^$',
        HomeView.as_view(template_name='pages/home.html'),
        name="home"),

    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    # about page
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # flat pages
    # url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^pages/', include('pages.urls', namespace='pages')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Uncomment the next line to enable avatars

    # Your stuff: custom urls go here
    # News
    url(r'^news/', include("news.urls", namespace="news")),
    url(r'^members/', include("members.urls", namespace="members")),
    url(r'^events/', include("events.urls", namespace="events")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
