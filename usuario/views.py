# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from produtos.models import Produto
from usuario.forms import UsuarioForm

def painel(request):
	produtos = Produto.objects \
	                  .filter(usuario=request.user) \
	                  .order_by('-data_criacao')
	
	qtd = produtos.count()

	return render(request, 'usuario/painel.html',{
		'produtos': produtos,
		'total_produtos': qtd,	
	})


def criar_usuario(request):
	form = UsuarioForm()
	return render(request, 'usuario/criar.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')