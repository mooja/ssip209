from django.views.generic import TemplateView
from datetime import datetime, timedelta

from news.models import NewsEntry
from swingtime.models import Occurrence


class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        within = datetime.now() + timedelta(weeks=8)
        upcoming_occurrence_list = Occurrence.objects.all().filter(start_time__lte=within)

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.all()
        context['upcoming_occurrence_list'] = upcoming_occurrence_list

        return context
