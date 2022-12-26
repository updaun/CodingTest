# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 시저 암호


def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        else:
            if i.islower():
                temp = ord(i) + n
                if temp > 122:
                    temp -= 26
                answer += chr(temp)
            else:
                temp = ord(i) + n
                if temp > 90:
                    temp -= 26
                answer += chr(temp)
    return answer

print(solution("AB", 1)) # BC
print(solution("z", 1)) # a
print(solution("a B z", 4)) # e F d