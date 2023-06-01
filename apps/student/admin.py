from django.contrib import admin
from .models import *

# Register your models here.

<<<<<<< HEAD

@admin.register(Student)
class 	StudentData(admin.ModelAdmin):
    list_display=('id','semester','major')

@admin.register(Enrollment)
class 	EnrollmentData(admin.ModelAdmin):
    list_display=('id','academic_period')

@admin.register(Student_Subject)
class Student_SubjectData(admin.ModelAdmin):
    list_display=('name','shift','schedule')
=======
>>>>>>> 944f203429d9e85b419c11df60451f28341062dc
