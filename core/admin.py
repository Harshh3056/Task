from django.contrib import admin
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4  

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserSubmission)
admin.site.register(UserAnswer)
admin.site.register(Event)
