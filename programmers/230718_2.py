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

# 다른 사람의 풀이
def solution(log):
    res=''
    # 딕셔너리를 활용하여 키값으로 접근
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res


q = solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])
assert q == "wsdawsdassw", "불일치"
print(q)
