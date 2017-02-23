from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^produto/$',views.ListarProdutos.as_view(), name = 'listar-produtos'),
    url(r'^$',views.ListarProdutos.as_view(), name = 'listar-produtos'),

]