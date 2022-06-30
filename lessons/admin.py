from django.contrib import admin
from .models import Lesson, Teacher

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['isActive', 'title', 'date']
    list_display_links = ('title',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['isActive', 'teacher']
    list_display_links = ('teacher',)
