from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'update_at')
    list_filter = ('created_at', 'update_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'update_at')
    
    # группировка полей на странице редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content')
        }),
        ('Даты', {
            'fields': ('created_at', 'update_at'),
            'classes': ('collapse',) # сворачиваемая секция
        }),
    )
