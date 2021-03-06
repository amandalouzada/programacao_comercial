"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from sistema import settings
from autenticacao import views
from evento.views import *
from participante.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.Index.as_view(), name="index"),
    url(r'^', include('autenticacao.urls')),
    url(r'^eventos/', include('evento.urls')),
    url(r'^participantes/', include('participante.urls')),
    url(r'^inscricao/', include('inscricao.urls'))
]
