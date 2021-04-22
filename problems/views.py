from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Problem, SolvedProblem
from .modules import Crawling

@require_safe
def index(request):
    # 전체 문제 번호
    problem_numbers = Problem.objects.all()

    context = {
        'problem_numbers': problem_numbers,
        
    }
    return render(request, 'problems/index.html', context)


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


# =================================개별 회원이 푼 한 문제의 코드 가져오기=================================
@require_safe
def user_problem_code(request, username, problem_number):
    solver = get_object_or_404(get_user_model(), username=username)
    problem = get_object_or_404(Problem, number=problem_number)
    solvedProblem = SolvedProblem.objects.filter(user=solver, problem=problem)
    solved_code = solvedProblem[0].solved_code
    
    # 이거 잘 모르겠음 solvedProblems manager로 불러오는 것은 solvedproblems 테이블인데 어떻게 필드를 number로 찾아 들어갈 수 있는지?
    # solvedproblems 테이블이 갖고 있는 것은 problem_id이기 때문에 먼저 problem 객체를 가져오고 그 뒤에 pk 값을 통해 찾아야 할 것 같은데 위와 같이 그냥 number로 접근이 가능한 이유를 모르겠음
    # problem = get_object_or_404(Problem, number=problem_number)
    
    context = {
        'solvedProblem': solvedProblem[0],
        'problem': problem,
        'solver': solver,
    }

    return render(request, 'problems/code.html', context)


# =================================개별 회원이 푼 한 문제의 코드 등록, 수정, 삭제하기=================================
# 코드 등록하기
@require_http_methods(['GET', 'POST'])
@login_required
def register_code(request, username, problem_number):
    solver = get_object_or_404(get_user_model(), username=username)
    if request.user != solver:
        return redirect('problems:user_problem_code', username, problem_number)
    else:
        if request.method == 'POST':
            problem = get_object_or_404(Problem, number=problem_number)
            solvedProblem = get_object_or_404(SolvedProblem, user=solver, problem=problem)
            solvedProblem.solved_code = request.POST.get('solved_code')
            solvedProblem.save()

            return redirect('problems:user_problem_code', username, problem_number)
        else:
            solver = get_object_or_404(get_user_model(), username=username)
            problem = get_object_or_404(Problem, number=problem_number)
        
        context = {
            'solver': solver,
            'problem': problem,
        }

        return render(request, 'problems/code_create.html', context)

# 코드 수정하기
@require_http_methods(['GET', 'POST'])
@login_required
def update_code(request, username, problem_number):
    solver = get_object_or_404(get_user_model(), username=username)
    problem = get_object_or_404(Problem, number=problem_number)
    solvedProblem = get_object_or_404(SolvedProblem, user=solver, problem=problem)

    if request.user != solver:
        return redirect('problems:user_problem_code', username, problem_number)
    else:
        if request.method == 'POST':
            solvedProblem.solved_code = request.POST.get('solved_code')
            solvedProblem.save()

            return redirect('problems:user_problem_code', username, problem_number)
        else:
            # get 방식 요청일 시에 이미 위에서 context로 넘길 변수들을 정의하였으므로 삭제해도 되나..?
            pass
        
        context = {
            'solver': solver,
            'problem': problem,
            'solvedProblem': solvedProblem,
        }

        return render(request, 'problems/code_update.html', context)