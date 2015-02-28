# -*- coding: utf-8 -*-
from django.shortcuts import render
from produtos.models import Produto

def painel(request):
	produtos = Produto.objects \
	                  .filter(usuario=request.user) \
	                  .order_by('-data_criacao')
	
	qtd = produtos.count()

	return render(request, 'usuario/painel.html',{
		'produtos': produtos,
		'total_produtos': qtd,	
	})