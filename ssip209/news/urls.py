# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    url(
        regex=r'^$',
        view=views.NewsEntryListView.as_view(),
        name='newsentry-list'
    ),
    url(
        regex=r'^(?P<slug>[\w_-]+)/$',
        view=views.NewsEntryDetailView.as_view(),
        name='newsentry-detail'
    ),
    # # URL pattern for the UserRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),
    # # URL pattern for the UserDetailView
    # # URL pattern for the UserUpdateView
    # url(
    #     regex=r'^~update/$',
    #     view=views.UserUpdateView.as_view(),
    #     name='update'
    # ),
)
