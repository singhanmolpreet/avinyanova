# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URLs
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
]