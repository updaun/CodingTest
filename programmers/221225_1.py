# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 3진법 뒤집기

def solution(n):
    answer = ""
    while n >= 3:
        n, s = divmod(n, 3)
        answer = str(s) + answer
    if n != 0:
        answer = (str(n) + answer)
    temp = 0
    for i in range(len(answer)):
        temp += int(answer[i])*3**i
    return temp

print(solution(45)) # 7
print(solution(125)) # 229