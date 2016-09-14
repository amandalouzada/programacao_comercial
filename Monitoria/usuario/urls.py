from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UsuarioIndex.as_view(), name='index'),
    url(r'^login/$', views.login, name='login')
]
