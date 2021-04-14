# BAEKTRACKING

서울 1반 알고리즘 스터디를 위한 백준 크롤링 사이트



## 기능

- [x] 전체 문제 크롤링 - DB 저장
- [x] 회원별 문제 크롤링 - DB 저장
- [ ] 일별 문제 크롤링
- [ ] problems/index.html
  - [ ] 문제 - 문제 푼 사람 리스트 출력(problems with solvers)
  - [ ] 문제 클릭 시 해당 문제를 푼 사람 리스트 + 코드

해당 문제를 푼 사람 검색

차트 - 푼 문제 / 전체 문제



## Database

> 향후 ERD로 업데이트
>
> <small>(임시) ['model name'] - ['field name']</small>

[User] - username, password, baekjoon_id, profile_image

[Problem] - number, difficulty

[SolvedProblems] - solved_code, solved_date, problem_id(FK), user_id(FK)



> username, problem_number도 pk어야 함 >> username을 통해 profile에 접근하고, problem_number를 통해 problem에 접근하기 때문



## 페이지

1. problems index
   - [ ] 문제(pagination), 문제 티어, 푼 사람 리스트
   
     