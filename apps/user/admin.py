from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import User, Event, Event_User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'name',
                    'lastname', 'active_user', 'admin_user')
    exclude = ('previous_user','previous_email')
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_init','date_finish','type', 'status')

@admin.register(Event_User)
class EventUserAdmin(admin.ModelAdmin):
    list_display = ('id_user','id_Event','permissions')