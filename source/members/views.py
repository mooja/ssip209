from django.views.generic import DetailView, ListView
from braces.views import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms

from django.conf import settings

from members.models import Member


# Create your views here.
class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    context_object_name = "member"
    template_name = "members/member_detail.html"


@require_http_methods(['GET', 'POST'])
def member_list(request):
    MEMBERS_PASSWORD = settings.MEMBERS_PASSWORD

    # handle form submission
    if request.POST:
        pw_form = PasswordForm(request.POST)

        if pw_form.is_valid() and pw_form.cleaned_data['password'] == MEMBERS_PASSWORD:
            request.session['password'] = pw_form.cleaned_data['password']
            return redirect('members:member-list')

        messages.error(request, "The password you entered was incorrect, please try again.")

    # form not being submitted, check password
    if (request.session.get('password') and request.session['password'] == MEMBERS_PASSWORD):
        member_list = Member.objects.all()
        return render(request, 'members/member_list.html', {
            'member_list': member_list,
        })

    # password is wrong, render form
    pw_form = PasswordForm()
    return render(request, 'members/members_password_form.html', {
        'pw_form': pw_form,
    })


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
    }))
