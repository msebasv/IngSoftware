from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Graduate, Job
from .forms import LaboralDataForm
from django.urls import reverse_lazy

# Create your views here.
class formDataJob(CreateView):
    model = Graduate
    template_name = 'data_form.html'
    form_class = LaboralDataForm
    success_url = reverse_lazy('graduates:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'graduate_results': self.request.session.get('graduate_results'),
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


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