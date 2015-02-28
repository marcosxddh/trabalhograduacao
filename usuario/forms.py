# -*- coding: utf-8 -*-
from django.forms import ModelForm
from produtos.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('datejoined', 'user_permissions', 'groups', 'active')