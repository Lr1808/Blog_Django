from django.shortcuts import render
from .models import publication
from django.views.generic import ListView
# Create your views here.


class PublicationListView(ListView):
    model = publication
    template_name = 'home.html'

    