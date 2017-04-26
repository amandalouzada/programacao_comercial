from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ParticipanteList.as_view(), name='listar-participante'),
    url(r'^novoUsuario/$', views.UsuarioCreate.as_view(), name='novo-usuario'),
    url(r'^novo/$', views.ParticipanteCreate.as_view(), name='novo-participante')

]
