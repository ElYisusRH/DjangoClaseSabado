from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class homepageView(TemplateView):
    template_name = "home.html"
class casapageView(TemplateView):
    template_name = "casa.html"

    