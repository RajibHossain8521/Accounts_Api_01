from django.contrib import admin
from .models import UserAccounts

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']

admin.site.register(UserAccounts, UserAdmin)