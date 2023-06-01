from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Administrative)
class AdministrativeData(admin.ModelAdmin):
    list_display=('id','position')

@admin.register(Comite)
class ComiteData(admin.ModelAdmin):
    list_display=('name','type')


@admin.register(Act)
class ActData(admin.ModelAdmin):
    list_display=('id','title','type','date_actual')