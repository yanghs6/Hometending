from django.contrib import admin
from .models import *


class HometendAdmin(admin.ModelAdmin):
    """모델 HometendUser의 admin
    
    Attributes:
        search_fields: username, first_name, email, date_joined, last_login
        list_display: username, first_name, email, date_joined, last_login
        list_filter: date_joined, last_login
    """
    search_fields = ['username', 'first_name', 'email', 'date_joined', 'last_login']
    list_display = ['username', 'first_name', 'email', 'date_joined', 'last_login']
    list_filter = ['date_joined', 'last_login']
    
admin.site.register(HometendUser, HometendAdmin)
    