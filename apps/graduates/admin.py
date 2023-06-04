from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Graduate)
class 	StudentData(admin.ModelAdmin):
    list_display=('salary_range','work_experience','student_id')
    exclude = ('job_id','position','salary_range','email','previous_email','achievement_level','work_experience','cv')