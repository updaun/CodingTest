# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 2016년

from datetime import date, timedelta
def solution(a, b):
    week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return week[date(2016, a, b).weekday()]


print(solution(5, 24)) # "TUE"
