from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),

    url(r'^visualizar/(?P<produto_id>\d+)/$', 'views.visualizar_produto',
    	name='visualizar_produto'),

    url(r'^produto/', include('produtos.urls', namespace='produtos')),

	url(r'^usuario/', include('usuario.urls', namespace='usuario')),

    url(r'^admin/', include(admin.site.urls))
)
