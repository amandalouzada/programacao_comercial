from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^usuario/$', views.UsuarioIndex.as_view(), name='index'),
    url(r'^usuario/listar/$', views.UsuarioList.as_view(), name='listar-usuario'),
    url(r'^usuario/login/$', views.login, name='login'),
    url(r'^usuario/novo/$', views.UsuarioNew.as_view(), name='novo-usuario'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioEdit.as_view(), name='editar-usuario'),
]
