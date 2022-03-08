from django.contrib import admin
from .models import Task, TaskStatus, TaskTag

admin.site.register(Task)
admin.site.register(TaskTag, list_display=('id', 'name'))
