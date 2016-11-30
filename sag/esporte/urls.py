from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^atleta/listar/$', views.AtletasList.as_view(), name='listar-atletas'),
]
