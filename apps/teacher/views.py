from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Teacher, Preg_Ev, Question
from django.db.models import Count
# Create your views here.

class results(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'teacher_results': self.request.session.get('teacher_results'),
        }
        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        # Obtener el usuario actual
        user = self.request.user

        # Obtener el objeto Student correspondiente al usuario actual
        teacher = Teacher.objects.get(user_id=user)
        results = Preg_Ev.objects.values('grade').annotate(total=Count('id')).order_by('grade')
        context['questions'] = Question.objects.all()
        context ['data'] = results
        context['teacher'] = teacher


        return context



class viewDataProfile(TemplateView):
    model = Teacher
    template_name = 'profile_teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'teacher_results': self.request.session.get('teacher_results'),
        }
        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        # Obtener el usuario actual
        user = self.request.user

        # Obtener el objeto Student correspondiente al usuario actual
        teacher = Teacher.objects.get(user_id=user)

        context['teacher'] = teacher


        return context