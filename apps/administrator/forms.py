from django import forms
from .models import Act, ActType

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
        required = {
            'committee': False,
            'type': False,
            'title': False,
            'description': False,
            'document': False,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtén el valor del comité seleccionado
        committee_id = self.instance.committee_id

        # Actualiza las opciones del campo de selección de actas
        self.fields['type'].widget.attrs['data-committee'] = committee_id












