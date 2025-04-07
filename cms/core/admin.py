from django.contrib import admin
from .models import Student
from .forms import StudentForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
