from django.shortcuts import render

from django.views.generic import DetailView, ListView
from braces.views import LoginRequiredMixin
from news.models import NewsEntry

# Create your views here.

class NewsEntryDetailView(LoginRequiredMixin, DetailView):
    model = NewsEntry
    context_object_name = "news_entry"
    template_name = "news/news_entry_detail.html"


class NewsEntryListView(ListView):
    model = NewsEntry
    context_object_name = "news_entry_list"
    template_name = "news/news_entry_list.html"
