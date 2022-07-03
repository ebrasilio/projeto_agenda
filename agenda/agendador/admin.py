from django.contrib import admin
from .models import Funcionario, Servico, Agendamento #, Cliente, 

# admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(Agendamento)