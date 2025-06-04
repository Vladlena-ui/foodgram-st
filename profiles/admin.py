from django.contrib import admin
from .models import CustomUser, Subscription
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(Subscription)
