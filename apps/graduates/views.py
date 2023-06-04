from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Graduate, Job
from apps.student.models import Student 
from django.urls import reverse_lazy

# Create your views here.

class formDataJob(TemplateView):
    template_name = 'data_form.html'
    success_url = reverse_lazy ('graduates:profile')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_results = {
            'graduate_results': self.request.session.get('graduate_results'),
        }
        context.update({key: value for key, value in session_results.items() if value})
        return context
    def post(self, request):
        student = Student.objects.get(user_id=request.user)
        tipo_empleo = request.POST.get('tipo_empleo')
        empresa = request.POST.get('empresa')
        sector = request.POST.get('sector')
        rango_salarial = request.POST.get('rango_salarial')
        cargo = request.POST.get('cargo')
        titulo = request.POST.get('titulo')
        experiencia = request.POST.get('experiencia_laboral')
        cv = request.FILES.get('hoja_vida')
        graduate = Graduate.objects.get(student_id=student)
        graduate.salary_range = rango_salarial
        graduate.achievement_level = titulo
        graduate.work_experience = experiencia
        graduate.position = cargo
        graduate.cv = cv
        graduate.save()
        job = graduate.job_id
        job.company = empresa
        job.sector = sector
        job.type = tipo_empleo
        job.save()
        
        return redirect(self.success_url)

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

        # Obtener el usuario actual
        user = self.request.user

        try:
            # Obtener el objeto Student correspondiente al usuario actual
            student = Student.objects.get(user_id=user)

            # Obtener el objeto Graduate correspondiente al objeto Student
            graduate = Graduate.objects.get(student_id=student)

            # Agregar el graduado al contexto
            context['graduate'] = graduate

            job = graduate.job_id
            context['job'] = job

        except Student.DoesNotExist or Graduate.DoesNotExist:
            # Manejar el caso en el que no exista un estudiante o graduado para el usuario actual
            context['graduate'] = None


        return context