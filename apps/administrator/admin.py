from django.contrib import admin
from .models import Committee, Act, ActType

# Register your models here.
class CommitteAdmin(admin.ModelAdmin):
  list_display = ('id','name')
  
class ActTypeAdmin(admin.ModelAdmin):
  list_display = ('id','name', 'committee')
  
class ActAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'type', 'description', 'current_date', 'modification_date', 'document', 'status', 'administrative_id', 'committee')
  
admin.site.register(Committee, CommitteAdmin)
admin.site.register(ActType, ActTypeAdmin)
admin.site.register(Act, ActAdmin)