"""news_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

# Auth Imports
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# App Imports 
from home.views import homeView
from stockMarket import views as stockMarket_views
from profiles import views as profiles_views

urlpatterns = [
    path("", homeView.as_view(), name="home_page"),

    # User paths
    path('register/', profiles_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="profiles/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="profiles/logout.html"), name="logout"),
    path('profile/<int:pk>',profiles_views.profile,name="profile"),
    path('profile/update', profiles_views.update, name="update"),
    
    #password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="profiles/password_reset.html"), name="password_reset"),
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="profiles/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name="profiles/password_reset_done.html"), name="password_reset_done"),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name="profiles/password_reset_complete.html"), name="password_reset_complete"),
    

    #stockMarket
    #path('stocks-dashboard/', stockMarket_views.stocksdashboard, name="stocks-dashboard"),
    path("stocks-dashboard/", login_required(stockMarket_views.stocksdashboard.as_view()), name="stocks-dashboard"),
    path("addportafolio/", login_required(stockMarket_views.addportafolio.as_view()), name="addportafolio"),
    path("addticker/", login_required(stockMarket_views.addticker.as_view()), name="addticker"),
    path("portafolio/<int:pk>", login_required(stockMarket_views.displayPortafolio.as_view()), name="portafolio"),
    path("stock/<int:pk>", login_required(stockMarket_views.displayStock.as_view()), name="stock"),


    #News

    # Admin
    path('admin/', admin.site.urls),
  
]

#Do note that this is not the preferred way of serving files in production.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)