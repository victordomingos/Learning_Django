from django import forms

from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ('titulo', 'texto',)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('autor', 'texto',)
