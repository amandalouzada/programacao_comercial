from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^credenciamento/(?P<pk>[\w-]+)$', views.Credenciamento.as_view(), name='credenciamento'),
    url(r'^credenciados/(?P<pk>[\w-]+)$', views.EventoListCredenciado.as_view(), name='credenciados'),
]
