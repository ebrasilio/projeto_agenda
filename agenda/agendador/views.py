# from distutils import core
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Agendamento
from .forms import AgendamentoForm


def home(request):
    return render(request, 'agendador/home.html')

def login_user(request):
    return render(request, 'agendador/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou Senha Inválidos ! ")      
        return redirect('/login')

@login_required(login_url = '/login/')
def listar(request):
    usuario = request.user
    eventos_lista = Agendamento.objects.filter(user = usuario).order_by('data_ag')
    #eventos_lista = Agendamento.objects.all().order_by('data_ag')
 
    paginator = Paginator(eventos_lista, 3)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)

    return render(request, 'agendador/lista.html', {'eventos':eventos})

# create
@login_required(login_url = '/login/')
def agendar(request):
    form = AgendamentoForm(request.POST or None)
    if form.is_valid():
        form.user = request.user
        form.save()
        return redirect('listar_evento')
    return render(request, 'agendador/agendar_form.html', {'form': form} )

# update - edit
@login_required
def update(request, pk):
    data = {}
    agenda = Agendamento.objects.get(pk=pk)
    form = AgendamentoForm(request.POST or None, instance=agenda)
    
    if form.is_valid():
        form.save()
        return redirect('listar_evento')

    data['form'] = form
    data['obj'] = agenda
    return render(request, 'agendador/agendar_form.html', data)

# delete
@login_required
def delete(request, pk):
    agenda = Agendamento.objects.get(pk=pk)
    agenda.delete()

    messages.info(request,"Agendamento Removido!!!")

    return redirect('listar_evento')


def cadastro_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_index')

    data['form'] = form
    return render(request, 'agenda/form.html', data)