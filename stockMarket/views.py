from email import message
from multiprocessing import context
from urllib import request
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from django.views.generic import TemplateView, FormView 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Portafolio
from .forms import RegisterTicker


from datetime import datetime   

from django.utils.decorators import method_decorator

from django.urls import reverse


# Create your views here.

class stocksdashboard(TemplateView):
    date_now = datetime.now()
    template_name = "stockMarket/Dashboard.html"    
    def get_context_data(self, **kwargs):
        context = super(stocksdashboard, self).get_context_data(**kwargs)
        try:
            p = Portafolio.objects.get(pk = self.request.user.pk)
        except:
            p=None

        context.update(
            {
                'date_now': self.date_now, 
                'user_in_stock': self.request.user.username,
                 'p': p
            }
        )
        return context    

class addticker(FormView):
    template_name = "stockMarket/addTicker.html"  
    form_class = RegisterTicker
   
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs) 

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        # here you can add things like:
        #context[show_results] = False
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        # here you can add things like:
        context['new_ticker'] = 'newwwww'
        messages.success(self.request, 'Your ticker was updated.') # ignored
        return self.render_to_response(context)