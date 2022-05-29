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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import from home app
from home.views import homeView
from django.views.generic.base import TemplateView # new
from profiles import views as profiles_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", homeView.as_view(), name="home_page"),
    path('register/', profiles_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="profiles/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="profiles/logout.html"), name="logout"),
    path('admin/', admin.site.urls),
  
]

#Do note that this is not the preferred way of serving files in production.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)