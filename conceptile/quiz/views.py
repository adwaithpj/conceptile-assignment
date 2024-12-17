from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, QuizSession, QuizSessionQuestion
from django.urls import reverse


@login_required
def start_quiz(request):
    return render(
        request,
        "quiz/start.html",
    )


@login_required
def redirect_start_quiz(request):
    quiz_session = QuizSession.objects.create(
        user=request.user, total_questions=0, correct_answers=0, incorrect_answers=0
    )
    print(quiz_session.id)
    return redirect("quiz:quiz", session_id=quiz_session.id)


@login_required
def quiz(request, session_id: int):

    try:
        quiz_session = QuizSession.objects.get(id=session_id, user=request.user)
    except QuizSession.DoesNotExist:
        # Handle case where session doesn't exist
        return redirect(reverse("quiz:start_quiz"))

    if quiz_session.is_completed is True:
        return redirect(reverse("quiz:quiz_results", kwargs={"session_id": session_id}))

    if request.method == "POST":
        question_id = request.POST.get("question_id")
        selected_choice_id = request.POST.get("choice")

        print(question_id, selected_choice_id)

        if question_id and selected_choice_id:
            question = get_object_or_404(Question, id=question_id)
            selected_choice = get_object_or_404(Choice, id=selected_choice_id)

            if not QuizSessionQuestion.objects.filter(
                session=session_id, question=question
            ).exists():
                is_correct = selected_choice.is_correct
                QuizSessionQuestion.objects.create(
                    session=quiz_session,
                    question=question,
                    selected_choice=selected_choice,
                    is_correct=is_correct,
                )

                quiz_session.total_questions += 1
                if is_correct:
                    quiz_session.correct_answers += 1
                else:
                    quiz_session.incorrect_answers += 1
                quiz_session.save()

    answered_questions = quiz_session.session_questions.values_list(
        "question_id", flat=True
    )
    question = Question.objects.exclude(id__in=answered_questions).order_by("?").first()
    # question = Question.objects.order_by("?").first()
    if not question or quiz_session.total_questions >= 20:
        quiz_session.is_completed = True
        quiz_session.save()
        return redirect(reverse("quiz:quiz_results", kwargs={"session_id": session_id}))

    choices = question.choices.all()

    return render(
        request,
        "quiz/quiz.html",
        {"question": question, "choices": choices, "quiz_session": quiz_session},
    )


@login_required
def quiz_results(request, session_id: int):
    quiz_session = get_object_or_404(QuizSession, id=session_id, user=request.user)
    quiz_session.is_completed = True
    quiz_session.save()

    # Fetch all questions answered in this session
    session_questions = quiz_session.session_questions.select_related(
        "question", "selected_choice"
    ).all()

    return render(
        request,
        "quiz/results.html",
        {"quiz_session": quiz_session, "session_questions": session_questions},
    )
