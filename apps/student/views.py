from django.shortcuts import redirect , HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Student
from apps.teacher.models import Evaluation , Teacher, Preg_Ev
from apps.teacher.models import Question
from .forms import TeacherForm
from django.contrib.sessions.models import Session
# Create your views here.

class early_Assessment(TemplateView):
    template_name = 'assessment_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.all()
        context['questions'] = questions
        context['evaluation'] = TeacherForm()
        session_results = {
            'student_results': self.request.session.get('student_results'),
        }
        context.update({key: value for key, value in session_results.items() if value})
        return context
    
    def post(self, request):
        session_results = self.request.session.get('student_results')
        if session_results[0]['completed'] is False:
            form = TeacherForm(request.POST)
            if form.is_valid():
                student = Student.objects.get(id=session_results[0]['id'])
                print('saddsadsadsasad'+student.major)
                student.completed = True
                student.save()
                user_teacher_id = form.cleaned_data['teacher']
                subject_id = form.cleaned_data['subject']
                teacher = Teacher.objects.filter(user_id=user_teacher_id).first()
                if teacher:
                    evaluation = Evaluation.objects.create(teacher_id_id=teacher.id, Subject_id_id=subject_id)
                    for question in Question.objects.all():
                        answer = request.POST.get(f'respuesta_{question.id}')
                        Preg_Ev.objects.create(id_evaluation_id=evaluation.id, id_question_id=question.id, grade=answer)
                    return redirect(self.success_url)
                
                else:
                    return HttpResponse("Error: No se encontró el profesor asociado al usuario.")
            else:
                return HttpResponse("Error en el formulario")
        else:
            return redirect('/dashboard')


class viewDataProfile(TemplateView):
    model = Student
    template_name = 'profile_students.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los resultados almacenados en la sesión del usuario
        session_results = {
            'student_results': self.request.session.get('student_results'),
        }
        # Agregar los resultados no nulos al contexto
        context.update({key: value for key, value in session_results.items() if value})

        # Obtener el usuario actual
        user = self.request.user

        # Obtener el objeto Student correspondiente al usuario actual
        student = Student.objects.get(user_id=user)

        context['student'] = student


        return context