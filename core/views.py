from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event
from django.contrib.auth.decorators import login_required

# Home page
def home(request):

    quizzes = Quiz.objects.all()
    events = Event.objects.all()
    return render(request, 'core/home.html', {
        'quizzes': quizzes,
        'events': events
    })


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'core/quiz_list.html', {'quizzes': quizzes})


def quiz_attempt(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        submission = None

        if request.user.is_authenticated:
            submission = UserSubmission.objects.create(
                quiz=quiz,
                user_name=request.user.username
            )

        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                answer = question.answers.get(id=int(selected_answer_id))
                is_correct = answer.is_correct
                if is_correct:
                    score += 1

                if submission:
                    UserAnswer.objects.create(
                        submission=submission,
                        question=question,
                        answer=answer.text,
                        is_correct=is_correct
                    )

        if submission:
            submission.score = score
            submission.save()

        total = questions.count()
        return render(request, 'core/result.html', {
            'quiz': quiz,
            'score': score,
            'total': total
        })

    return render(request, 'core/quiz_attempt.html', {
        'quiz': quiz,
        'questions': questions
    })

def result(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user_result = None

    if request.user.is_authenticated:
        user_result = UserSubmission.objects.filter(
            user_name=request.user.username, quiz=quiz
        ).last()

    score = user_result.score if user_result else 0
    total = quiz.questions.count()

    return render(request, 'core/result.html', {
        'quiz': quiz,
        'score': score,
        'total': total
    })

def events(request):
    events = Event.objects.all()
    return render(request, 'core/events.html', {'events': events})
