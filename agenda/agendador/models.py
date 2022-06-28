from django.db import models
from django.contrib.auth import get_user_model

class Cliente(models.Model):
    nome_cli = models.CharField(max_length=100)
    nasc_cli = models.DateField()
    cpf_cli = models.IntegerField()
    tel_cli = models.CharField(max_length=15)  # formatar e verificar 
    email_cli = models.EmailField()
    sex_cli = models.CharField(max_length=1)   # aplicar criterio
    dt_cadastro = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome_cli

class Funcionario(models.Model):
    nome_fun = models.CharField(max_length=100)
    cpf_fun = models.IntegerField()
    tel_fun = models.CharField(max_length=15)  # formatar e verificar 
    email_fun = models.EmailField()
    status_fun = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_fun

class Servico(models.Model):
    nome_ser = models.CharField(max_length=20)
    desc_ser = models.TextField(verbose_name='Descrição')
    val_ser = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_ser

class Agendamento(models.Model):
    data_ag = models.DateTimeField()
    profis  = models.ForeignKey(Funcionario, on_delete = models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete = models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.data_ag
