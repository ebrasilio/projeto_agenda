from django.contrib import admin
from .models import Cliente, Funcionario, Servico, Agendamento

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(Agendamento)