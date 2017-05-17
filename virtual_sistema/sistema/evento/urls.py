from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventoList.as_view(), name='listar-eventos'),
    url(r'^pdf/(?P<pk>[\w-]+)$', views.Pdf.as_view(), name='pdf'),
    url(r'^pdfBarcode/(?P<pk>[\w-]+)$', views.PdfBarcode.as_view(), name='pdf-barcode'),
    url(r'^inscricoes/(?P<pk>[\w-]+)$', views.EventoListInscricao.as_view(), name='inscricoes-evento'),
    url(r'^novo/$', views.EventoCreate.as_view(), name='novo-evento'),
    url(r'^update/(?P<pk>[\w-]+)$', views.EventoUpdate.as_view(), name='update-evento'),
    url(r'^novaProgramacao/(?P<pk>[\w-]+)$', views.ProgramacaoCreate.as_view(), name='nova-programcao'),
    url(r'^listProgramacao/(?P<pk>[\w-]+)$', views.ProgramacaoList.as_view(), name='lista-programcao'),
    url(r'^detalhe/(?P<pk>[\w-]+)$', views.EventoDetalhe.as_view(), name='detalhe-evento'),
]
