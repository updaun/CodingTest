# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 문자열 나누기

def solution(s):
    answer = 0
    temp_a = 0
    temp_b = 0
    for i in range(len(s)):
        if temp_a == 0:
            temp = s[i]
            temp_a += 1
        else:
            if temp == s[i]:
                temp_a += 1
            else:
                temp_b += 1
            if temp_a == temp_b:
                answer += 1
                temp_a = 0
                temp_b = 0
    if temp_a != 0:
        answer += 1
    return answer

print(solution("banana")) # 3
print(solution("abracadabra")) # 6
print(solution("aaabbaccccabba")) # 3