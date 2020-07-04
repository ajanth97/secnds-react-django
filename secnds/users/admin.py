from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'last_login', 'date_joined',
                    'is_active', 'is_staff', 'is_admin')
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)

    filter_horizontal = ()
    list_filter = ('is_admin', 'is_staff', 'is_active')
    fieldsets = ()
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),)


admin.site.register(User, AccountAdmin)
