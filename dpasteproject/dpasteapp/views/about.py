from django.shortcuts import redirect
from django.views.generic import TemplateView


class aboutView(TemplateView):
    template_name = 'about.html'