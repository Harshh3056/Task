from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_view

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('home', views.home, name='home'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:pk>/', views.quiz_attempt, name='quiz_attempt'),
    path('result/<int:pk>/', views.result, name='result'),
    path('events/', views.events, name='events'),
    path('register/', register_view, name='register'),
]

