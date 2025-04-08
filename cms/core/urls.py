from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('upload/academic/', views.upload_academic_record, name='upload_academic'),
    path('upload/extracurricular/', views.upload_extra_curricular, name='upload_extra'),
    path('upload/sports/', views.upload_sports_achievement, name='upload_sports'),
    path('student/academic_success/', views.academic_success, name='academic_success'),
    path('student/extra_success/', views.extra_success, name='extra_success'),
    path('student/sports_success/', views.sports_success, name='sports_success'),
]
