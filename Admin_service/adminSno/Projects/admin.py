from django.contrib import admin
from .models import *
# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'stage', 'notes']
    search_fields = ['name']
    list_filter = ['create_id', 'stage']
    filter_horizontal = ['persons']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'link', 'rate', 'courses']
    search_fields = ['name']
    list_filter = ['create_id', 'courses', 'position', 'knowledgeLevel']
    filter_horizontal = ['project']


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Courses)
admin.site.register(TasksProjects)