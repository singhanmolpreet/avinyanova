from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('verify_login_otp/', views.verify_login_otp, name='verify_login_otp'),
    path('logout/',views.LogoutPage,name='logout')
]
