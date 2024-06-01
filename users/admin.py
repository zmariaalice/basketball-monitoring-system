from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'last_login', 'total_time_spent']
    search_fields = ['username', 'email']
    list_filter = ['role']
