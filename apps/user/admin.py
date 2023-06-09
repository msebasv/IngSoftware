from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import User, Event, Event_User
from django.contrib.auth.hashers import make_password

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'name',
                    'lastname', 'active_user', 'admin_user')
    exclude = ('previous_user','previous_email')
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            # Si la contraseña ha sido modificada, encriptarla
            obj.password = make_password(form.cleaned_data['password'])
        obj.save()
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_init','date_finish','type', 'status')

@admin.register(Event_User)
class EventUserAdmin(admin.ModelAdmin):
    list_display = ('id_user','id_Event','permissions')