from django.shortcuts import render
from datetime import datetime 
from django.views.generic import TemplateView   

# # Create your views here.
# class homeView(TemplateView):
#     template_name = "home/Index.html"

class homeView(TemplateView):
    date_now = datetime.now()
    template_name = "home/Index.html"

    def get_context_data(self, **kwargs):
        context = super(homeView, self).get_context_data(**kwargs)
        context.update({'date_now': self.date_now})
        return context    