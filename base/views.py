from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'base/index.html'
    

class WorksView(TemplateView):
    template_name = 'base/works.html'
    
    
class NewsView(TemplateView):
    template_name = 'base/news.html'