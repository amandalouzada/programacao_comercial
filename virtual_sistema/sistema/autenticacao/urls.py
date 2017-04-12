from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Autenticacao.as_view(), name='login'),
    url(r'^logout/', views.Logout.as_view(), name='logout'),
    url(r'^$', views.Index.as_view(), name='index')
]
