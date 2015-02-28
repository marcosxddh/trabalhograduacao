# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from produtos.forms import ProdutoForm
from produtos.models import Produto
from django.core.files import File


def form(request):
    produtos = Produto.objects.filter(valido=1).order_by('data_criacao')

    if request.method == 'GET':
        usuario = {'usuario': request.user}
        form = ProdutoForm(initial=usuario)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = request.user
            form.save(usuario)
            messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            return redirect('usuario:painel')

    return render(request, 'produtos/form.html', {
        'form': form,
        'produtos': produtos
    })


def editar_produto(request, produto_id):
    produtos = Produto.objects.filter(usuario=request.user) \
                              .order_by('nome')
    if request.method == 'GET':
        produto = Produto.objects.get(pk=produto_id)
        usuario = {'usuario': request.user}
        form = ProdutoForm(initial=usuario, instance=produto)

    if request.method == 'POST':
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            usuario = request.user
            form.save(usuario)
            messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            return redirect('usuario:painel')

    return render(request, 'produtos/form.html',{
        'form': form,
        'produtos': produtos
    })

def excluir_produto(request):
    if request.method == 'POST':
        try:
            produto_id = request.POST.get('produto_id')
            produto = Produto.objects.get(pk=produto_id)
            produto.valido = 0
            produto.save()
            messages.add_message(request, messages.SUCCESS, 'Produto excluido com sucesso!')
        except Exception:
            messages.add_message(request, messages.ERROR, 'Não foi possível excluir o produto!')
    return redirect('usuario:painel')