from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'name',
                    'lastname', 'active_user', 'admin_user')
    add_form = CustomUserCreationForm


admin.site.register(User, UserAdmin)