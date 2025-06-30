from django.contrib import admin
from .models import TeacherInfo

class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ('category', 'faculties_required', 'faculties_available', 'deficiency')
    list_filter = ('category',)  # Add any filtering options you need
    search_fields = ('category',)  # Add any fields you want to search by

admin.site.register(TeacherInfo, TeacherInfoAdmin)
