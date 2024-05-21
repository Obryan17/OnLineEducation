from django.contrib import admin
from .models import Course , Lesson

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at')
    search_fields = ('title', 'instructor_username') 
    list_filter = ('instructor', 'created_at')

@admin.register(Lesson)    
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course', )
    search_fields = ('title', 'course_title')
    
""" class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','first_name','last_name')
    list_filter = ('is_staff','is_superuser','is_active')
    
admin.site.register( CustomUser , CustomUserAdmin ) """