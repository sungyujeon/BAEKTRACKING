from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('', views.index, name='index'),
    path('crawl_users/', views.crawl_all_users_solved_problems, name='crawl_all_users_solved_problems'),
    path('crawl_user/<baekjoon_id>/', views.crawl_a_user_solved_problems, name='crawl_a_user_solved_problems'),

]