# -*- coding: utf-8 -*-
from django.forms import ModelForm
from produtos.models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        exclude = ('valido', 'usuario')

    def save(self, usuario, *args, **kwargs):
    	instance = self.instance
    	instance.valido = 1
    	instance.usuario = usuario
    	super(ProdutoForm, self).save(*args, **kwargs)

