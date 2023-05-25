from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView, View
from .models import Act
# Create your views here.

class CreateAct(TemplateView):
    model = Act
    template_name = 'data_form_act.html'
    # success_url = reverse_lazy('dashboard')

class ListAct(TemplateView):
    model = Act
    template_name = 'list_act.html'