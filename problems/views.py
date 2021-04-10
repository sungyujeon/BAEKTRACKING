from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Problem
from . modules import Crawling
from bs4 import BeautifulSoup
import requests

def index(request):
    return render(request, 'problems/index.html')

# =================================모든 회원의 푼 문제 크롤링=================================
@require_safe
@login_required
def crawl_all_users_solved_problems(request):
    users = get_user_model().objects.all()

    for user in users:
        # 해당 유저가 푼 문제 목록 가져오기
        crawling = Crawling()
        user_problems_list = crawling.get_users_solved_problems_list(user.baekjoon_id)
        
        # 해당 유저가 푼 문제들을 db에 저장
        for problem_number in user_problems_list:
            problem, created = Problem.objects.get_or_create(number=problem_number)
            user.solvedProblems.add(problem)
        
    return redirect('problems:index')



# =================================개별 회원의 푼 문제 크롤링=================================
@require_safe
@login_required
def crawl_a_user_solved_problems(request, baekjoon_id):
    user = get_object_or_404(get_user_model(), baekjoon_id=baekjoon_id)

    # 해당 유저가 푼 문제 목록 가져오기
    crawling = Crawling()
    user_problems_list = crawling.get_users_solved_problems_list(user.baekjoon_id)
    
    # 해당 유저가 푼 문제들을 db에 저장
    for problem_number in user_problems_list:
        problem, created = Problem.objects.get_or_create(number=problem_number)
        user.solvedProblems.add(problem)
        
    return redirect('problems:index')

