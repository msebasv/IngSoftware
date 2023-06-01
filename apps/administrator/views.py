from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView, View
from .models import Act
# Create your views here.

class CreateAct(TemplateView):
    model = Act
    template_name = 'data_form_act.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'administrative_results': self.request.session.get('administrative_results')
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context

class ListAct(TemplateView):
    model = Act
    template_name = 'list_act.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'administrative_results': self.request.session.get('administrative_results'),
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context