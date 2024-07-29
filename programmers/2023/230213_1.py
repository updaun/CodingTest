# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for case in babbling:
        s = []
        temp = ""
        for i in case:
            temp += i
            if temp in can:
                if len(s) > 0 and s[-1] == temp:
                    temp = ""
                s.append(temp)
                temp = ""
        if len(case) == sum([len(i) for i in s]):
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa"]))  # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # 1
