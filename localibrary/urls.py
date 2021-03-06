"""localibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalogo/', include('catalogo.urls')),
    #
    url(r'^prueba/', views.prueba),
    url(r'^$', views.index),
    
    #url(r'^dif/[0-9]{2}', include('catalogo.urls')),
    #url('', RedirectView.as_view(url='/catalogo/', permanent=True)),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
