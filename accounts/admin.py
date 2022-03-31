from django.contrib import admin
from .models import AuthUserManager, AuthUser


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = AuthUser
        fields = ('username', 'date_joined',  'admin', 'last_login')
        readonly_fields = ('date_joined',)
    list_filter = ('admin',)
    ordering = ('username',)
    search_fields = ('username',)
    filter_horizontal = ()


admin.site.register(AuthUser, UserAdmin)
