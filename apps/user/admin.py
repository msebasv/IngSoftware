from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'name',
                    'lastname', 'active_user', 'admin_user')
    exclude = ('previous_user','previous_email')
