from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView
from .forms import FormLogin
from .models import Event, Event_User
from apps.administrator.models import Administrative
from apps.student.models import Student
from apps.graduates.models import Graduate
from apps.teacher.models import Teacher
# Create your views here.

class Dashboard(ListView):
    # model = Event
    model = Event_User
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.id

        if Administrative.objects.filter(user_id=user).exists():
            administrative_results = Administrative.objects.filter(user_id=user)
            self.request.session['administrative_results'] = list(administrative_results.values())
            context['administrative_results'] = administrative_results

        elif Student.objects.filter(user_id=user).exists():
            student_results = Student.objects.filter(user_id=user)
            self.request.session['student_results'] = list(student_results.values())
            context['student_results'] = student_results

            student = student_results.first().id

            if Graduate.objects.filter(student_id=student).exists():
                graduate_results = Graduate.objects.filter(student_id=student)
                self.request.session['graduate_results'] = list(graduate_results.values())
                context['graduate_results'] = graduate_results

        elif Teacher.objects.filter(user_id=user).exists():
            teacher_results = Teacher.objects.filter(user_id=user)
            self.request.session['teacher_results'] = list(teacher_results.values())
            context['teacher_results'] = teacher_results
        return context
    
    def get_queryset(self):
        user = self.request.user
        queryset = Event.objects.filter(event_user__id_user=user)
        return queryset




class Login(FormView):
    template_name = 'index.html'
    form_class = FormLogin
    success_url = reverse_lazy('dashboard')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


