# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > OX퀴즈

def solution(quiz):
    answer = []
    for q in quiz:
        x, t, y, e, r = q.split()
        if "-" in r:
            r = int(r[1:]) * -1
        else:
            r = int(r)
        if t == "+":
            if int(x) + int(y) == r:
                answer.append("O")
            else:
                answer.append("X")
        elif t == "-":
            if int(x) - int(y) == r:
                answer.append("O")
            else:
                answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"])) # ["X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])) # ["O", "O", "X", "O"]