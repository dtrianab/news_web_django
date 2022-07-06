from logging import exception
from unicodedata import name
from django.contrib import messages
from django.views.generic import TemplateView, FormView 
from .models import Portafolio, Stock
from .forms import RegisterPortafolio, RegisterTicker
from datetime import datetime   
from django.db.models.expressions import Func
from yfinance import Ticker 

from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect



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
    success_url="stocks-dashboard/"
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
        if val in str(P_user_names):
            messages.success(self.request, 'Portafolio name:'+ str(val) +' is already existing.')
            return self.render_to_response(context)
        else:
            messages.success(self.request, 'Adding new Portafolio')    
            form_new = Portafolio()   
            form_new.user = self.request.user
            form_new.name = val
            form_new.country = self.request.POST.get('country')
            form_new.save() 
            messages.success(self.request, 'Portafolio: ' + val + ' stored') # ignored
            #return render(self.request, "stockMarket/dashboard.html", {"user": self.request.user})    
            #return reverse('stocks-dashboard')
            return redirect('stocks-dashboard')
        
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
        val = self.request.POST.get('tag')
        #Check if ticker exists in DB 
        if Stock.objects.filter(ticker=val).first() == None :
            try:
                # Try to find ticker in Yahoo finance
                new_ticker = Ticker(val)
                new_stock = Stock(ticker = val, name=new_ticker.info['shortName'])
                new_stock.save()
                Portafolio.objects.filter(user = self.request.user).update(userStock = new_stock)
                messages.success(self.request, 'Ticker' + new_ticker.info['shortName'] + ' added') # ignored
            except: 
                messages.error(self.request, 'Can not find ticker '+ val +' at Yahoo Finance') # ignored   
        else:
            # Ticker already in DB
            val_stock = Stock.objects.filter(ticker = val).first()
            P = Portafolio.objects.filter(user = self.request.user).first()
            P.userStock.add(val_stock.id)
            messages.success(self.request, 'Ticker '+ val  +' already existing in DB. Added to Portafolio'  ) # ignored    
        return self.render_to_response(context)

class displayPortafolio(TemplateView):
    template_name = "stockMarket/portafolio.html"
    def get_context_data(self, **kwargs): 
        context = super(displayPortafolio, self).get_context_data(**kwargs)
        pk_sel = context['pk']
        P = Portafolio.objects.filter(pk=pk_sel).first()
        pname = P.name
        s = P.userStock.all()
        context.update(
            {
             'pname': pname,
             's': s
             }
        )
        return context  

class displayStock(TemplateView):
    template_name = "stockMarket/stock.html"
    def get_context_data(self, **kwargs): 
        context = super(displayStock, self).get_context_data(**kwargs)
        # pk_sel = context['pk']
        # P = Portafolio.objects.filter(pk=pk_sel).first()
        # pname = P.name
        
        # s = P.userStock.all()
        

        # context.update(
        #     {
        #      'pname': pname,
        #      's': s
        #      }
        # )
        return context  
