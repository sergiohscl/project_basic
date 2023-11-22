from django import forms
from plataforma.models import Livros


class Livro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"

    # Esta é uma maneira de mudar os campos input do nosso formulario.
    # Outra maneira se encontra na views.

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['nome'].widget.attrs['class'] = 'form-control'
    #     self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
