from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventoList.as_view(), name='listar-eventos'),
    url(r'^inscricoes/(?P<pk>[\w-]+)$', views.EventoListInscricao.as_view(), name='inscricoes-evento'),
    url(r'^novo/$', views.EventoCreate.as_view(), name='novo-evento'),
    url(r'^detalhe/(?P<pk>[\w-]+)$', views.EventoDetalhe.as_view(), name='detalhe-evento'),
]
