from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ListarMesas.as_view(), name = 'listar-mesas'),
    url(r'^novo$',views.NovaMesa.as_view(), name = 'cadastrar-mesa'),
    url(r'^novasMesas$',views.novasMesas),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdateMesa.as_view(), name = 'update-produto'),
]
