from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from django.http import HttpResponse
from django.views import View
import datetime

# def home(request):
#     #now = datetime.datetime.now()
#     #html = "<html><body>It is now %s.</body></html>" % now
#     return render(request, "index.html", {})

class home(View):
    now = datetime.datetime.now()
    def get(self, request):
        return render(request, "index.html",{'time_now':self.now})

class AboutView(TemplateView):
    template_name = "about.html"         