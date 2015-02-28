from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^painel$', 'usuario.views.painel', name='painel'),
)