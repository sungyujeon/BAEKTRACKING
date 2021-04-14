from django.contrib import admin
from .models import Problem, SolvedProblem

# Register your models here.
admin.site.register(Problem)
admin.site.register(SolvedProblem)