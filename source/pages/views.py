import markdown

from django.views.generic import DetailView
from .models import Page


class PageDetailView(DetailView):
    """ 
        simple static view. 
        can render markdown or reStructured text
    """

    model = Page
    context_object_name = 'page'
    template_name = 'pages/page_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        if self.object.text_format == 'markdown':
            md = markdown.Markdown(extensions=['markdown.extensions.toc'])
            html = md.convert(context['page'].text)
            toc = md.toc

            context['page'].text = html
            context['page'].toc = toc

        return context
