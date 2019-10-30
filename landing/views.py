from django.shortcuts import render
from django.views.generic import TemplateView


class LandPageIndex(TemplateView):
    template_name = 'landing/index.html'
