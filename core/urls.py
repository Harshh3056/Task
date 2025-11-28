from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:pk>/', views.quiz_attempt, name='quiz_attempt'),
    path('result/<int:pk>/', views.result, name='result'),
    path('events/', views.events, name='events'),
]
