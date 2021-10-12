from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('password1')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Logado')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email1 = request.POST.get('email1')
    usuario = request.POST.get('usuario')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if not name or not surname or not email1 or not usuario or not password1 \
or not password2:
        messages.error(request, 'Você precisa preencher todos os campos')
        return render(request, 'accounts/register.html')
    try:
        validate_email(email1)
    except:
        messages.error(request, 'E-mail invalido.')
        return render(request, 'accounts/register.html')
    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')
    if len(password1) < 6 or len(password2) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')
    if password1 != password2:
        messages.error(request, 'As senhas não são iguais')
        return render(request, 'accounts/register.html')
    if User.objects.filter(username=usuario).exists():
        return render(request, 'Usuario já existe')
    if User.objects.filter(email=email1).exists():
        return render(request, 'E-mail já existe')
    messages.success(request, 'Registrado com sucesso! Faça seu login.')
    user = User.objects.create_user(username=usuario, email=email1, password=password1, first_name=name,last_name=surname)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form })
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição insuficiente')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contato {request.POST.get("name")} Salvo com sucesso')
    return redirect('dashboard')