from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^form/$', 'produtos.view.form', 
    	name='criar_produto'),

    url(r'^editar/(?P<produto_id>\d+)/$', 'produtos.view.editar_produto', 
    	name='editar_produto'),

    url(r'^excluir/$', 'produtos.view.excluir_produto', 
    	name='excluir_produto'),
)