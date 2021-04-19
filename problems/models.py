from django.db import models
from django.conf import settings

class Site(models.Model):
    site = models.CharField(max_length=30, default='백준')

class Problem(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
    number = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    solvedUsers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='solvedProblem', related_name='solvedProblems')


class SolvedProblem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    solved_code = models.TextField()
    solved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user}, problem:{self.problem}, solved_date:{self.solved_date}, solved_code:{self.solved_code}'