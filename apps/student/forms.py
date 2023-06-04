from django import forms
from apps.teacher.models import Evaluation, Teacher, Subject

class TeacherForm(forms.Form):
    teacher = forms.ChoiceField(
        choices=[],
        label='Profesor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    subject = forms.ChoiceField(
        choices=[],
        label='Asignatura',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        teachers = Teacher.objects.select_related('user_id').values_list('user_id__id', 'user_id__name', 'user_id__lastname', 'user_id__email')
        teacher_choices = [(teacher[0], f'{teacher[2]} {teacher[1]}') for teacher in teachers]
        self.fields['teacher'].choices = teacher_choices

        subjects = Subject.objects.values_list('id', 'name')
        subject_choices = [(subject[0], subject[1]) for subject in subjects]
        self.fields['subject'].choices = subject_choices