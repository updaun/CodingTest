# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 옹알이 (1)

can = ["aya", "ye", "woo", "ma"]
def check(my_string):
    for i in can:
        if i in my_string:
            return i
    return None

def solution(babbling):
    answer = 0
    for t in babbling:
        while True:
            s = check(t)
            if s:
                t = t.replace(s,str(can.index(s)))
            else:
                break
        if t.isdigit():
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"])) # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) # 3