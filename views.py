# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.files import File
from django.contrib import messages
from produtos.models import Categoria, Regiao, Produto


def index(request):
    categoria_id = request.POST.get('categoria_id')
    categorias = Categoria.objects.all()
    regioes = Regiao.objects.all()

    if categoria_id == None:
        produtos = Produto.objects.filter(valido=1).order_by('data_criacao')

    else:
        produtos = Produto.objects.filter(categoria=categoria_id).order_by('data_criacao')
        
        if len(produtos) == 0:
            messages.add_message(request, messages.INFO, 'Não foram encontrados produtos nesta categoria, tente novamente!')

    lista = []

    for produto in produtos:
        foto = produto.foto.url
        foto = str(foto)[12:]
        dados = {
            'produto': produto,
            'foto': foto
        }
        lista.append(dados)

    return render(request, 'index.html', {
        'categorias': categorias,
        'regioes': regioes,
        'dados': lista
    })


def visualizar_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    foto = produto.foto.url
    foto = str(foto)[12:]
    return render(request, 'produtos/visualizar.html',{
        'produto': produto,
        'foto': foto
    })