# 프로그래머스
# 코딩테스트 연습 > 정렬 > 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    num_list = list(map(str, numbers))
    num_list.sort(key=lambda x:x*3, reverse=True)
    return str(int("".join(num_list)))

# 정렬을 할 때 문제의 값 범위를 활용하여 가장 큰 수를 만들기 위한 정렬
# 마지막에 숫자형태로 바꿨다가 다시 문자열로 변경
