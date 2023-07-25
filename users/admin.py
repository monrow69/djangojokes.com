from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from common.admin import DjangoJokesAdmin

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(DjangoJokesAdmin, UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )