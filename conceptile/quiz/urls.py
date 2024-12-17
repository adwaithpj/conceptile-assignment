from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("start/", views.start_quiz, name="start_quiz"),
    path("questions/<int:session_id>/", views.quiz, name="quiz"),
    path("results/<int:session_id>/", views.quiz_results, name="quiz_results"),
    path("create-session/", views.redirect_start_quiz, name="redirect_start_quiz"),
    # path("results/", views.quiz_results, name="quiz_results"),
]
