from django import forms
from .models import Act, ActType
from apps.user.models import Event, Event_User, User

class ActForm(forms.ModelForm):
    class Meta:
        model = Act
        fields = ['committee', 'type', 'title', 'description', 'document']
        widgets = {
            'committee': forms.Select(attrs={'class': 'form-control', 'id': 'id_committee'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'id_type'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'committee': 'Comité',
            'type': 'Tipo de Acta',
            'title': 'Título',
            'description': 'Descripción',
            'document': 'Archivo',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtén el valor del comité seleccionado
        committee_id = self.instance.committee_id

        # Actualiza las opciones del campo de selección de actas
        self.fields['type'].widget.attrs['data-committee'] = committee_id

class EventForm(forms.ModelForm):
    id_user = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuario')
    class Meta:
        model = Event
        fields = ['type', 'subject', 'date_init', 'time_init', 'date_finish', 'time_finish', 'description']
        labels = {
            'type': 'Tipo de evento',
            'subject': 'Tema',
            'date_init': 'Fecha de inicio',
            'time_init': 'Hora de inicio',
            'date_finish': 'Fecha de Fin',
            'time_finish': 'Hora de Fin',
            'description': 'Descripción'
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'select_tipo'}),
            'subject': forms.TextInput(attrs={'class': 'input_subject'}),
            'date_init': forms.DateInput(attrs={'class': 'input_fecha_inicio', 'type': 'date'}),
            'time_init': forms.TimeInput(attrs={'class': 'input_hora_inicio', 'type': 'time'}),
            'date_finish': forms.DateInput(attrs={'class': 'input_fecha_fin', 'type': 'date'}),
            'time_finish': forms.TimeInput(attrs={'class': 'input_hora_fin', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'textarea_descripcion', 'rows': 3}),
            'id_user': forms.Select(attrs={'class': 'select_user'}),
        }     













