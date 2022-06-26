from distutils import core
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Agendamento
from .forms import AgendamentoForm

def helloworld(request):
    return HttpResponse('<h1>Hello World!</h1>')

def home(request):
    return render(request, 'agendador/home.html')

def yourName(request, name):
    return render(request, 'agendador/yourname.html', {'name': name} )

def listar(request):
    eventos_lista = Agendamento.objects.all().order_by('data_ag')
    paginator = Paginator(eventos_lista, 3)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)

    return render(request, 'agendador/lista.html', {'eventos':eventos})


# create
def agendar(request):
    form = AgendamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_evento')
    return render(request, 'agendador/agendar_form.html', {'form': form} )

# update - edit
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