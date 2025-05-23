from django.contrib import admin
from content_app.models import Content, Playlist

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public')
    list_filter = ('content_type', 'is_public')
    ordering = ('-upload_date')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'file_url', 'thumbnail_url', 'content_type', 'upload_date', 'views', 'likes', 'is_public', 'status')
    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
  )

admin.site.register(Content)
admin.site.register(Playlist)