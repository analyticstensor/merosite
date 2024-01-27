from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm 
    add_form = CustomUserCreationForm
           
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active']

    # fieldsets = (
    #     (None, {'fields': ['email', 'password']}),
    #     ("Personal info", {'fields': ['first_name']}),
    # )
    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'],
            }                    
        )
    ]

admin.site.register(CustomUser, CustomUserAdmin)
