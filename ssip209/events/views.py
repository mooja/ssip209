from django.contrib.auth.decorators import login_required
from swingtime.views import *

# Create your views here.
view_view = login_required(event_view)
event_listing = login_required(event_listing)
occurrence_view = login_required(occurrence_view)
add_event = login_required(add_event)
