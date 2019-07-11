from django.contrib import admin
from .models import Profile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegistrationForm, UserEditForm


class UserAdmin(BaseUserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name', 'is_innovator', 'is_investor', 'is_entrepreneur')}
         ),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2')
        }),
    )
    list_filter = ['is_innovator', 'is_investor', 'is_entrepreneur', 'is_superuser']

    form = UserEditForm
    add_form = UserRegistrationForm


admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']


admin.site.register(Profile, ProfileAdmin)
