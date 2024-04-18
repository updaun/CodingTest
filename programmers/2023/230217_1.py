# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = '0'
    temp = 1
    remain = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while len(answer) <= t*m:
        s = temp
        s_str = ""
        while s:
            s, r = divmod(s, n)
            if r > 9:
                s_str = remain[r] + s_str
            else:
                s_str = str(r) + s_str
        answer += s_str
        temp += 1
    result = ""
    for i in range(p-1, len(answer), m):
        result += answer[i]
        if len(result) == t:
            break
    return result


print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
