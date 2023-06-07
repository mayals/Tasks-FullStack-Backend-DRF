from django.contrib import admin

# Register your models here.

from .models import Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ["t_name","t_created",]
    list_display = ["t_name","t_created",]
    readonly_fields = ("t_created",)