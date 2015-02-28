# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Produto(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    marca = models.CharField(max_length=100)
    valor = models.FloatField()
    categoria = models.ForeignKey('Categoria')
    foto = models.ImageField(upload_to='base/static/fotos', blank=True, null=True)
    usuario = models.ForeignKey('Usuario')
    valido = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valido = models.IntegerField()

    def __unicode__(self):
        return u'%s' %self.nome


class Regiao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __unicode__(self):
        return u'%s' %self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.nome


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    regiao = models.ForeignKey(Regiao)
    cidade = models.ForeignKey(Cidade)

    def __unicode__(self):
        return u'%s' % self.nome


class Usuario(User):
    sexo = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'))
    endereco = models.ForeignKey(Endereco)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=12)
    sexo = models.CharField(choices=sexo, max_length=20)

    def __unicode__(self):
        return u'%s' % self.nome


admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Regiao)
admin.site.register(Endereco)
admin.site.register(Cidade)
admin.site.register(Usuario)