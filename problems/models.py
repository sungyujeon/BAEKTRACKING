from django.db import models
from django.conf import settings

class Problem(models.Model):
    number = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    solvedUsers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='solvedProblems', related_name='solvedProblems')


class SolvedProblems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solved_code = models.TextField()
    solved_date = models.DateTimeField(auto_now_add=True)