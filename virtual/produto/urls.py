from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^produto/$',views.ListarProdutos.as_view(), name = 'listar-produtos'),
    url(r'^$',views.ListarProdutos.as_view(), name = 'listar-produtos'),
    url(r'^novo/$',views.NovoProduto.as_view(), name = 'cadastrar-produto'),
    url(r'^update/(?P<pk>[\w-]+)$',views.UpdateProduto.as_view(), name = 'update-produto'),
    url(r'^novoImagem/$',views.NovoImagem.as_view(), name = 'cadastrar-imagem'),
    url(r'^(?P<tipo_produto>[\w-]+)$',views.ListarProdutosTipo.as_view(), name = 'listar-produtos-tipo'),
]
