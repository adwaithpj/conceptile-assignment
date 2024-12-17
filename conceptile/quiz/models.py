from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuizSession(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Quiz Session for {self.user.username}"


class QuizSessionQuestion(models.Model):
    session = models.ForeignKey(
        QuizSession, on_delete=models.CASCADE, related_name="session_questions"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(
        Choice, null=True, blank=True, on_delete=models.SET_NULL
    )
    is_correct = models.BooleanField(default=False)
