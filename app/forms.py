from django import forms

class  eventForm (forms.Form):
    name = forms.CharField(label='Nombre',required='True',max_length=20)
    email=forms.CharField(label='Email',required=True,max_length=30)
    content =forms.CharField(label='contenido', max_length=400, widget=forms.Textarea)