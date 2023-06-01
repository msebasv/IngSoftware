from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)
class 	StudentData(admin.ModelAdmin):
    list_display=('id','semester','major')

@admin.register(Enrollment)
class 	EnrollmentData(admin.ModelAdmin):
    list_display=('id','academic_period')

@admin.register(Student_Subject)
class Student_SubjectData(admin.ModelAdmin):
    list_display=('name','shift','schedule')
