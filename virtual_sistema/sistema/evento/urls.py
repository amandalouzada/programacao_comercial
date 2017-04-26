from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventoList.as_view(), name='listar-eventos'),
    url(r'^novo/$', views.EventoCreate.as_view(), name='novo-evento')
]
