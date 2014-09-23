from django.views.generic import DetailView, ListView
from members.models import Member

# Create your views here.
class MemberDetailView(DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member_detail.html"


class MemberListView(ListView):
    model = Member
    context_object_name = "member_list"
    template_name = "members/members_list.html"
