from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserForm)
class UserFormModel(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Age', 'Phone', 'Email', 'About']