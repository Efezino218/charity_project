from django.contrib import admin
from .models import Program, Blog

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_filter = ('location',)
    search_fields = ('title', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'location', 'video_url', 'video_file')
        }),
    )
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Blog, BlogAdmin)