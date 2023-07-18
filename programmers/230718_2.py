# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 수 조작하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181925


def solution(numLog):
    answer = ""
    for i in range(len(numLog)-1):
        temp = numLog[i+1] - numLog[i]
        if temp == 1:
            answer += "w"
        elif temp == -1:
            answer += "s"
        elif temp == 10:
            answer += "d"
        else:
            answer += "a"
    return answer


q = solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])
assert q == "wsdawsdassw", "불일치"
print(q)
