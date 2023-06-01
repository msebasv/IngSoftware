from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Graduate, Job

# Create your views here.
class formDataJob(TemplateView):
    model = Graduate
    template_name = 'data_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'graduate_results': self.request.session.get('graduate_results'),
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context


class viewDataProfile(TemplateView):
    model = Graduate
    template_name = 'profile_graduates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'graduate_results': self.request.session.get('graduate_results'),
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context