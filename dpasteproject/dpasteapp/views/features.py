from django.shortcuts import redirect
from django.views.generic import TemplateView


class featuresView(TemplateView):
    template_name = 'features.html'