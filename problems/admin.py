from django.contrib import admin
from .models import Problem, SolvedProblem, Site

# Register your models here.
admin.site.register(Problem)
admin.site.register(SolvedProblem)
admin.site.register(Site)
