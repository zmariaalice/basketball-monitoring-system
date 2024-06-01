from django.contrib import admin
from .models import Login

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ['user', 'login_time', 'logout_time']
    search_fields = ['user__username']
    list_filter = ['login_time']
