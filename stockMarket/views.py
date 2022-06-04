from unicodedata import name
from django.contrib import messages
from django.views.generic import TemplateView, FormView 
from .models import Portafolio, Stock
from .forms import RegisterPortafolio, RegisterTicker
from datetime import datetime   
from django.db.models.expressions import Func
from yfinance import Ticker 

# Create your views here.

class stocksdashboard(TemplateView):
    date_now = datetime.now()
    template_name = "stockMarket/Dashboard.html"    
    def get_context_data(self, **kwargs):
        context = super(stocksdashboard, self).get_context_data(**kwargs)
        p = Portafolio.objects.filter(user = self.request.user)
        m1 = ""
        if p.count() == 0:
            m1 = "No Portafolio yet"
        else: 
            m1 = str(p.count())    
        context.update(
            {
                'date_now': self.date_now, 
                'user_in_stock': self.request.user.username,
                'm1': m1,
                'p':p
            }
        )
        return context    

class addportafolio(FormView):
    template_name = "stockMarket/addportafolio.html"
    #success_url="stocks-dashboard/"
    form_class = RegisterPortafolio
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
        # form_class = self.get_form_class()
        # form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        val = self.request.POST.get('name')
        #form.save()    
        P_user = Portafolio.objects.filter(user = self.request.user)
        P_user_names = P_user.values_list('name')
        if P_user.count() != 0:
            if val in str(P_user_names):
                messages.success(self.request, 'Portafolio name:'+ str(val) +' is already existing.')
                return self.render_to_response(context)
        else:
            form_new = Portafolio()   
            form_new.user = self.request.user
            form_new.name = val
            form_new.country = self.request.POST.get('country')
            form_new.save() 
            messages.success(self.request, 'Portafolio: ' + val + ' stored') # ignored
            return self.render_to_response(context)

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
        #check if ticker exitsts
        val = self.request.POST.get('tag')
        #ticker exists? valid ? 
        if Stock.objects.filter(ticker=val).first() == None :
            new_ticker = Ticker(val)
            messages.success(self.request, 'Ticker' + new_ticker.info['shortName'] + ' not existing') # ignored
        else:
            messages.success(self.request, 'Ticker' + val ) # ignored    
        
        #in Portafolio?
        #messages.success(self.request, 'Ticker' + val + ' already in Portafolio') # ignored
        return self.render_to_response(context)

class displayPortafolio(TemplateView):
    template_name = "stockMarket/portafolio.html"
    def get_context_data(self, **kwargs): 
        context = super(displayPortafolio, self).get_context_data(**kwargs)
        pk_sel = context['pk']
        P = Portafolio.objects.filter(pk=pk_sel).first()
        pname = P.name
        context.update(
            {
             'pname': pname,
             }
        )
        return context  
