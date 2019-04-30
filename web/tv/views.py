from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Live(TemplateView):
    template_name = 'tv/player.html'