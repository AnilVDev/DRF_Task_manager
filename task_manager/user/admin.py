from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]


admin.site.register(CustomUser, CustomUserAdmin)
