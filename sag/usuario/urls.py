from django.conf.urls import url
from . import views #views no mesmo diretorio

urlpatterns = [
    url(r'^$', views.Usuario.as_view(), name='login'), # chama a tela de login quando a url eh /login
    url(r'^sair/', views.Logout.as_view(), name='sair'), # chama a classe Index quando a url eh /
]
