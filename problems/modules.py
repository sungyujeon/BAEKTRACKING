import requests
from bs4 import BeautifulSoup

class Crawling():

    def __init__(self):
        pass

    def get_users_solved_problems_list(self, baekjoon_id):
        user_profile_url = f'https://www.acmicpc.net/user/{baekjoon_id}'
        user_solved_problems_selector = 'body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body > a'

        res = requests.get(user_profile_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        problem_numbers = soup.select(user_solved_problems_selector)

        problem_list = []
        for problem_number in problem_numbers:
            problem_list.append(problem_number.get_text())
        
        return problem_list