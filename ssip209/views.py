from django.views.generic import TemplateView

from news.models import NewsEntry


class HomeView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['news_entry_list'] = NewsEntry.objects.all()
        return context
