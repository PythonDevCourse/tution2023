from django.shortcuts import render
from django.template import context
from .models import Accounts
from django.views.generic import ListView

# Create your views here.


def view(request):
    accounts = Accounts.objects.all()
    context = dict()
    context["accounts"] = accounts
    context["name"] = "I'm Muzzy"
    return render(template_name="accounts_list.abs", request=request, context=context)


class AccountListView(ListView):
    model = Accounts
