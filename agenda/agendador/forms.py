from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data_ag', 'cliente', 'servico', 'profis']
        labels = {'data_ag': 'Data', 'servico': 'Procedimento',
                  'profis': 'Profissional' }

        data_ag = forms.DateTimeField (
            widget = forms.DateTimeInput(format = '%d-%m-%Y %H', 
                attrs = {'class':'datepicker'}),
            input_formats=('%d-%m-%Y %H',) )
        