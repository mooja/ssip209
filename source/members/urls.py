from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    url(
        regex=r'^$',
        view=views.member_list,
        name='member-list'
    ),
    url(
        regex=r'^(?P<slug>[\w_-]+)/$',
        view=views.MemberDetailView.as_view(),
        name='member-detail'
    ),
)
