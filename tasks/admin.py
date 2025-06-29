from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'user']
    search_fields = ['title', 'description', 'user__name', 'user__email']
    ordering = ['-created_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'user', 'completed')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    