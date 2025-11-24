from django.db import models

# Create your models here.
from django.db import models

class QuizQuestion(models.Model):
    question = models.CharField(max_length=255)

    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)

    correct_answer = models.CharField(
        max_length=255,
        help_text="Must match one of the three answers."
    )

    def __str__(self):
        return self.question
