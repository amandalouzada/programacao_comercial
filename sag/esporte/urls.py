from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^atleta/$', views.Atletas.as_view(), name='atleta'),
    url(r'^atleta/listar/$', views.AtletasList.as_view(), name='listar-atletas'),
    url(r'^atleta/novo/$', views.AtletaNovo.as_view(), name='novo-atleta'),
]
