from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    # url(r'^atleta/novo/$', views.atleta),
    # url(r'^atleta/listar/$', views.listar),
    url(r'^atleta/listar/$', views.ListarAtleta.as_view(), name='listar-atletas'),
    url(r'^atleta/novo/$', views.NovoAtleta.as_view(), name='novo-atleta'),
    url(r'^atleta/deletar/(?P<pk>[\w-]+)$', views.DeletarAtleta.as_view(), name='deletar-atleta'),
    url(r'^tecnico/listar/$', views.ListarTecnico.as_view(), name='listar-tecnicos'),
    url(r'^tecnico/novo/$', views.NovoTecnico.as_view(), name='novo-tecnico'),
    url(r'^tecnico/deletar/(?P<pk>[\w-]+)$', views.DeletarTecnico.as_view(), name='deletar-tecnico'),
    url(r'^modalidade/listar/$', views.ListarModalidade.as_view(), name='listar-modalidades'),
    url(r'^modalidade/novo/$', views.NovoModalidade.as_view(), name='novo-modalidade'),
    url(r'^modalidade/deletar/(?P<pk>[\w-]+)$', views.DeletarModalidade.as_view(), name='deletar-modalidade'),

]
