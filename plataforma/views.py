from django.shortcuts import render
from plataforma.forms import Livro
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login')
def home(request):
    if request.method == 'GET':
        form = Livro()
        input_alterar = ('nome_livro')
        for i in form.fields.keys():
            if i in input_alterar:
                form.fields[i].widget.attrs['class'] = "form-control-sm"
                placeholder = ''
                if i == 'nome_livro':
                    placeholder = 'Digite nome do livro'
                form.fields[i].widget.attrs['placeholder'] = placeholder
        return render(request, 'home.html', {'form': form})
    elif request.method == 'POST':
        form = Livro(request.POST)
        if form.is_valid():
            form.save()
            form = Livro()
            messages.add_message(
                request, constants.SUCCESS, 'Formulário enviado com sucesso!'
            )
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'home.html', {'form': form})
