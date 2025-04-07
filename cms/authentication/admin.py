from django.contrib import admin
from .models import CustomUser,studentProfile,teacherProfile

admin.site.register(CustomUser)
admin.site.register(studentProfile)
admin.site.register(teacherProfile)