from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Exeat, Security, Profile, ExeatExtension, Program


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active',
                    'is_admin', 'is_student', 'is_security', 'is_exeat_team')
    list_filter = ('is_staff', 'is_active', 'is_admin', 'is_student',
                   'is_security', 'is_exeat_team')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        (
            'Permissions',
            {'fields': ('is_staff', 'is_active', 'is_admin', 'is_student', 'is_security', 'is_exeat_team')}),
        (
            'User Details',
            {'fields': ('first_name', 'last_name')}
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2')}
         ),
        (
            'User Details', {
                'fields': (
                    'first_name', 'last_name'
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_staff', 'is_active', 'is_admin', 'is_student', 'is_security',
                    'is_exeat_team'
                )}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Exeat)
admin.site.register(Security)
admin.site.register(Profile)
admin.site.register(ExeatExtension)
admin.site.register(Program)
