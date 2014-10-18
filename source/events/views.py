from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from swingtime.views import *
from .models import SSIPOccurrence, Location


# Create your views here.
# view_view = login_required(event_view)
# event_listing = login_required(event_listing)
# add_event = login_required(add_event)

occurrence_view = occurrence_view


class SSIPOccurrenceDetailView(TemplateView):
    template_name = "events/occurrence_detail.html"

    def get_context_data(self, *args, **kwargs):
        pk = kwargs['pk']
        event_pk = kwargs['event_pk']

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['occurrence'] = get_object_or_404(
                                    SSIPOccurrence,
                                    pk=pk, event__pk=event_pk)

        return context


class LocationDetailView(DetailView):
    model = Location
    template_name = "events/location_detail.html"
    context_object_name = "loc"
