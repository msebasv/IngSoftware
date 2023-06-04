from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Teacher)
class TeacherData(admin.ModelAdmin):
    list_display=('id','faculty')
