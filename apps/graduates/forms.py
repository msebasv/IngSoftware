from django import forms
from .models import Job, Graduate


class LaboralDataForm(forms.ModelForm):
    class Meta:
        model = Job  # Replace 'Job' with your actual model class
        fields = '__all__'
    achievement_level = forms.CharField(label='Título profesional', max_length=100, widget=forms.TextInput(attrs={'class': 'my-custom-class'}))
    salary_Range = forms.ChoiceField(label='Campo salarial', choices=[ ('', 'Selecciona una opción'),
        ('$1.000.000 - $3.000.000', 'Entre $1.000.000 - $3.000.000'),
        ('$3.000.000 - $6.000.000', 'Entre $3.000.000 - $6.000.000'),
        ('$6.000.000 - $9.000.000', 'Entre $6.000.000 - $9.000.000'),
        ('$12.000.000 - $3.000.000', 'Entre $1.000.000 - $3.000.000'),
        ('$10.000.000 o más', '$10.000.000 o más'),], widget=forms.Select(attrs={'class': 'my-custom-class'}))
    position = forms.CharField(label='Cargo actual', max_length=100, widget=forms.TextInput(attrs={'class': 'my-custom-class'}))
    work_experience = forms.IntegerField(label='Experiencia', widget=forms.NumberInput(attrs={'class': 'my-custom-class'}))
    cv = forms.FileField(label='Hoja de vida', widget=forms.FileInput(attrs={'class': 'my-custom-class'}))
    def clean_hoja_de_vida(self):
        hoja_de_vida = self.cleaned_data['cv']
        if hoja_de_vida:
            if not hoja_de_vida.name.endswith('.pdf'):
                raise forms.ValidationError('El archivo debe tener extensión .pdf')
        return hoja_de_vida
    email = forms.EmailField(label='Correo adicional', widget=forms.EmailInput(attrs={'class': 'my-custom-class'}))

class companyDataForm(forms.ModelForm):
    class Meta:
        model = Graduate  # Replace 'Job' with your actual model class
        fields = '__all__'
    Sector = forms.CharField(label='Sector empresarial', max_length=250, widget=forms.TextInput(attrs={'class': 'form_group_input'}))
    Company = forms.CharField(label="Nombre empresa", max_length=250, widget=forms.TextInput(attrs={'class': 'form_group_input'}))
    type = forms.ChoiceField(label='Tipo de empleo', choices=[
        ('', 'Selecciona una opción'),
        ('Jornada completa', 'Jornada completa'),
        ('Jornada parcial', 'Jornada parcial'),
        ('Autónomo', 'Autónomo'),
        ('Profesional independiente', 'Profesional independiente'),
        ('Contrato temporal', 'Contrato temporal'),
        ('Contrato de prácticas', 'Contrato de prácticas'),
        ('Contrato de formación', 'Contrato de formación'),
        ('Temporal', 'Temporal'),
    ], widget=forms.Select(attrs={'class': 'form_group_select'}))