from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^painel$', 'usuario.views.painel', name='painel'),

    url(r'^criar-usuario$', 'usuario.views.criar_usuario', name='criar_usario'),

    url(r'^sair$', 'usuario.views.logout_view', name='logout'),
)