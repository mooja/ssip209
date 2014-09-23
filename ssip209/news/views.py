from django.views.generic import DetailView, ListView
from news.models import NewsEntry

# Create your views here.

class NewsEntryDetailView(DetailView):
    model = NewsEntry
    context_object_name = "news_entry"
    template_name = "news/news_entry_detail.html"


class NewsEntryListView(ListView):
    model = NewsEntry
    context_object_name = "news_entry_list"
    template_name = "news/news_entry_list.html"
