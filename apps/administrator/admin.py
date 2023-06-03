from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Administrative)
class AdministrativeData(admin.ModelAdmin):
    list_display=('id','position')

@admin.register(Committee)
class ComiteData(admin.ModelAdmin):
  list_display = ('id','name')

@admin.register(ActType)  
class ActTypeAdmin(admin.ModelAdmin):
  list_display = ('id','name', 'committee')

@admin.register(Act)    
class ActData(admin.ModelAdmin):
  list_display = ('id', 'title', 'type', 'description', 'current_date', 'modification_date', 'document', 'status', 'administrative_id', 'committee')