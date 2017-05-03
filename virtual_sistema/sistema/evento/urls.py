from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventoList.as_view(), name='listar-eventos'),
    url(r'^novo/$', views.EventoCreate.as_view(), name='novo-evento'),
    url(r'^detalhe/(?P<pk>[\w-]+)$', views.EventoDetalhe.as_view(), name='detalhe-evento'),
    url(r'^inscricao/(?P<pk>[\w-]+)$', views.EventoInscricao.as_view(), name='inscricao-evento')
]
