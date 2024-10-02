from django.contrib import admin
from .models import Task, SubTask, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'deadline')
    search_fields = ('title', 'status')
    list_filter = ('status', 'created_at')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'deadline', 'task')
    search_fields = ('title', 'status')
    list_filter = ('status', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



