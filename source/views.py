from django.views.generic import TemplateView
from datetime import datetime, timedelta
from pytz import timezone

from news.models import NewsEntry
from swingtime.models import Occurrence


class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        eastern_tz = timezone('US/Eastern')
        upper_bound = datetime.now(tz=eastern_tz) + timedelta(weeks=1)
        lower_bound = datetime.now(tz=eastern_tz) - timedelta(days=0)
        upcoming_occurrence_list = Occurrence.objects.all(
                ).filter(start_time__gte=lower_bound
                ).filter(start_time__lte=upper_bound)
        now = datetime.now(tz=eastern_tz)

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.all()
        context['upcoming_occurrence_list'] = upcoming_occurrence_list
        context['now'] = now

        return context
