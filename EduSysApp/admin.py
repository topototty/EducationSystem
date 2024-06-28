from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')
    search_fields = ('first_name', 'last_name', 'user__username')

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('specialization_name', 'specialization_code')
    search_fields = ('specialization_name', 'specialization_code')

@admin.register(StudyGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_number', 'specialization')
    search_fields = ('group_number', 'specialization__specialization_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group')
    search_fields = ('first_name', 'last_name', 'group__group_number')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',)
    search_fields = ('room_number',)

@admin.register(DayOfWeek)
class DayOfWeekAdmin(admin.ModelAdmin):
    list_display = ('day_name',)
    search_fields = ('day_name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name',)
    search_fields = ('subject_name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade_value', 'grade_date')
    search_fields = ('student__first_name', 'student__last_name', 'subject__subject_name', 'grade_value', 'grade_date')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('group', 'subject', 'day_of_week', 'start_time', 'end_time', 'lesson_status')
    search_fields = ('group__group_number', 'subject__subject_name', 'day_of_week__day_name', 'start_time', 'end_time', 'lesson_status')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_number',)
    search_fields = ('course_number',)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'lesson_status', 'request_status')


