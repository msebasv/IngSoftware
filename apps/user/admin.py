from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import User, User_General


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    list_display = ('username', 'email', 'name',
                    'lastname', 'active_user', 'admin_user')
<<<<<<< HEAD
    exclude = ('revious_user','previous_email','password')
=======
    add_form = CustomUserCreationForm


admin.site.register(User, UserAdmin)

@admin.register(User_General)
class adminUserGerneral(admin.ModelAdmin):
    list_display = ('name','institutional_user','email')

    exclude=('previous_email','previous_user')
>>>>>>> 944f203429d9e85b419c11df60451f28341062dc
