from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import *
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('email', 'username', 'name',
                    'lastname', 'active_user', 'admin_user')
    add_form = CustomUserCreationForm


admin.site.register(User, UserAdmin)



