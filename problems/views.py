from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Problem
from bs4 import BeautifulSoup
import requests

def index(request):
    return render(request, 'problems/index.html')

@require_safe
@login_required
def crawl_all_users_solved_problems(request):
    users = get_user_model().objects.all()

    for user in users:
        # 해당 유저가 푼 문제 목록 가져오기
        user_problems_list = get_users_solved_problems_list(user.baekjoon_id)
        
        # 해당 유저가 푼 문제들을 db에 저장
        for problem_number in user_problems_list:
            problem, created = Problem.objects.get_or_create(number=problem_number)
            user.solvedProblems.add(problem)
        
    return redirect('problems:index')


def get_users_solved_problems_list(baekjoon_id):
    user_profile_url = f'https://www.acmicpc.net/user/{baekjoon_id}'
    user_solved_problems_selector = 'body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body > a'

    res = requests.get(user_profile_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    problem_numbers = soup.select(user_solved_problems_selector)

    problem_list = []
    for problem_number in problem_numbers:
        problem_list.append(problem_number.get_text())
    
    return problem_list