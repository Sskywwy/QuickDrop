from django.contrib import admin
from .models import File
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload_at')
    search_fields = ('file',)
# Register your models here.
