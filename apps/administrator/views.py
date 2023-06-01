from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView, View, FormView
from django.contrib import messages
from django.db.models import F, Q
from .models import Act, Committee, ActType
from .forms import ActForm
import json
from django.http import JsonResponse
# Create your views here.

class ListAct(ListView):
    model = Act
    template_name = 'list_act.html'
    context_object_name = 'acts'
    paginate_by = 10
    committees = Committee.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['current_page_number'] = page_obj.number

        # Obtener la lista de comités y pasarla al contexto
        context['committees'] = self.committees

        # Obtener el ID del comité seleccionado
        selected_committee_id = self.request.GET.get('committee')

        # Obtener la lista de tipos de acta asociados al comité seleccionado
        if selected_committee_id:
            act_types = ActType.objects.filter(committee_id=selected_committee_id)
        else:
            act_types = ActType.objects.none()

        context['act_types'] = act_types

        # Obtener el ID del acta seleccionado
        selected_act_id = self.request.GET.get('act')

        # Establecer el comité y acta seleccionados en el contexto
        context['selected_committee_id'] = selected_committee_id
        context['selected_act_id'] = selected_act_id
        
        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'administrative_results': self.request.session.get('administrative_results'),
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=True).order_by('-id')  # Ordenar por id
        search_query = self.request.GET.get("search")
        committee_id = self.request.GET.get("committee")
        act_id = self.request.GET.get("act")

        # Filtrar por comité y acta si se seleccionaron
        if committee_id:
            queryset = queryset.filter(committee_id=committee_id)
        if act_id:
            queryset = queryset.filter(type_id=act_id)

        # Filtrar por búsqueda si se ingresó
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

class CreateAct(CreateView):
    model = Act
    template_name = 'data_form_act.html'
    form_class = ActForm
    success_url = reverse_lazy('administrator:list_act')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['act_types_by_committee'] = json.dumps(self.get_act_types_by_committee())
                # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'administrative_results': self.request.session.get('administrative_results')
        }

        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        return context

    def get_act_types_by_committee(self):
        act_types_by_committee = {}
        committees = Committee.objects.all()
        for committee in committees:
            act_types = ActType.objects.filter(committee=committee)
            act_types_by_committee[committee.id] = [act_type.id for act_type in act_types]
        return act_types_by_committee
    
    def form_valid(self, form):
        response = super().form_valid(form)
        acta_id = self.object.id
        return JsonResponse({'acta_id': acta_id})