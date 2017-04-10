from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ListarPedidos.as_view(), name = 'listar-pedidos'),
    url(r'^novo$',views.NovoPedido.as_view(), name = 'cadastrar-pedido'),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdatePedido.as_view(), name = 'update-pedido'),
    url(r'^deletar/(?P<pk>[\w-]+)$',views.DeletarPedido.as_view(), name = 'deletar-pedido'),
]
