# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from collections import deque


def solution(msg):
    answer = []
    q = deque(msg)
    s_dict = {chr(i): i-64 for i in range(ord("A"), ord("Z")+1)}
    temp = ""
    while q:
        while temp == "" or temp in s_dict.keys():
            if q:
                temp += q.popleft()
            else:
                if temp in s_dict.keys():
                    answer.append(s_dict[temp])
                    temp = ""
                break
        if temp != "":
            s_dict[temp] = max(s_dict.values()) + 1
            answer.append(s_dict[temp[:-1]])
            temp = temp[-1]
    if temp != "":
        answer.append(s_dict[temp])
    return answer

print("KAKAO") # [11, 1, 27, 15]
print("TOBEORNOTTOBEORTOBEORNOT") # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print("ABABABABABABABAB")  # [1, 2, 27, 29, 28, 31, 30]
