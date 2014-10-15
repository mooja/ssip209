from django.views.generic import TemplateView
from django.shortcuts import render_to_response

from datetime import datetime, timedelta
from pytz import timezone

from news.models import NewsEntry
from swingtime.models import Occurrence


def upcoming_events_query():
    eastern_tz = timezone('US/Eastern')
    now = datetime.now(tz=eastern_tz)

    upper_bound = now + timedelta(weeks=4)
    lower_bound = now - timedelta(days=0)
    upcoming_occurrence_list = Occurrence.objects.all(
            ).filter(start_time__gte=lower_bound
            ).filter(start_time__lte=upper_bound
            ).exclude(event__event_type__abbr='week',
                      start_time__gte=(now + timedelta(weeks=1)))

    return upcoming_occurrence_list


def render_sidebar_html(template="sidebar.html"):
    """ returns sidebar's rendered html as string """
    eastern_tz = timezone('US/Eastern')
    now = datetime.now(tz=eastern_tz)

    context = dict()
    context['upcoming_occurrence_list'] = upcoming_events_query()
    context['now'] = now

    return render_to_response(template, context).content

class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.all()
        context['sidebar_html'] = render_sidebar_html()

        return context
