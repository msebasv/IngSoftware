from django import forms
from django import forms

class LaboralDataForm(forms.Form):
    titulo = forms.CharField(label='Título profesional', max_length=100)
    cargo = forms.CharField(label='Cargo actual', max_length=100)
    tipo_empleo = forms.ChoiceField(label='Tipo de empleo', choices=[
        ('', 'Selecciona una opción'),
        ('Jornada completa', 'Jornada completa'),
        ('Jornada parcial', 'Jornada parcial'),
        ('Autónomo', 'Autónomo'),
        ('Profesional independiente', 'Profesional independiente'),
        ('Contrato temporal', 'Contrato temporal'),
        ('Contrato de prácticas', 'Contrato de prácticas'),
        ('Contrato de formación', 'Contrato de formación'),
        ('Temporal', 'Temporal'),
    ])
    empresa = forms.CharField(label='Empresa', max_length=100)
    sector = forms.CharField(label='Sector', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 3}))
    hoja_de_vida = forms.FileField(label='Hoja de vida')
    campo_salarial = forms.ChoiceField(label='Campo salarial', choices=[
        ('', 'Selecciona una opción'),
        ('Menos de 1000', 'Menos de 1000'),
        ('1000 - 2000', '1000 - 2000'),
        ('2000 - 3000', '2000 - 3000'),
        ('3000 - 4000', '3000 - 4000'),
        ('4000 - 5000', '4000 - 5000'),
        ('Más de 5000', 'Más de 5000'),
    ])

    def clean_hoja_de_vida(self):
        hoja_de_vida = self.cleaned_data['hoja_de_vida']
        if hoja_de_vida:
            if not hoja_de_vida.name.endswith('.pdf'):
                raise forms.ValidationError('El archivo debe tener extensión .pdf')
        return hoja_de_vida