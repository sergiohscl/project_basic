from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth import get_user_model

User = get_user_model()


def login(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/plataforma/home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    avatar = request.POST.get('avatar')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(
            request, constants.ERROR, 'Campo nome e email não podem estar vazio.'  # noqa E501
        )
        return redirect('/auth/cadastro/')

    if len(senha) < 8:
        messages.add_message(
            request, constants.ERROR, 'Sua senha deve ter no mínimo 8 caracteres.'  # noqa E501
        )
        return redirect('/auth/cadastro/')

    # if User.objects.filter(email=email).exists():
    #     messages.add_message(
    #         request, constants.ERROR, 'Email já cadastrado!'
    #     )
    #     return redirect('/auth/cadastro/')

    if User.objects.filter(username=nome).exists():
        messages.add_message(
            request, constants.ERROR, 'Usuário já cadastrado!'
        )
        return redirect('/auth/cadastro/')

    try:
        avatar = request.FILES.get('avatar')
        usuario = User.objects.create_user(
            username=nome, email=email, password=senha, avatar=avatar
        )
        usuario.save()
        messages.add_message(
            request, constants.SUCCESS, 'Usuário cadastrado com sucesso!'
        )
        return redirect('/auth/cadastro/')
    except Exception:
        messages.add_message(
            request, constants.ERROR, 'Erro interno do sistema!'
        )
        return redirect('/auth/cadastro/')


def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    usuario = auth.authenticate(request, username=nome, password=senha)

    if not usuario:
        messages.add_message(
            request, constants.WARNING, 'Usuario ou senha inválido!'
        )
        return redirect('/auth/login/')
    else:
        auth.login(request, usuario)
        return redirect('/plataforma/home')


def sair(request):
    auth.logout(request)
    messages.add_message(
        request, constants.WARNING, 'Faça login antes de acessar a plataforma!'
    )
    return redirect('/auth/login')
