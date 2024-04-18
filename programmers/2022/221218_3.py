# 프로그래머스
# 코딩테스트 연습 > 코딩테스트 입문 > 다항식 더하기

def solution(polynomial):
    answer = polynomial.split(" + ")
    x = 0
    k = 0
    for i in answer:
        if "x" in i:
            if i[:-1] == "":
                x += 1
            else:
                x += int(i[:-1])
        else:
            k += int(i)
    if x == 0:
        return str(k)
    elif k == 0:
        if x == 1:
            return "x"
        return f"{x}x"
    if x == 1:
        return f"x + {k}"
    else:
        return f"{x}x + {k}"

print(solution("3x + 7 + x")) # "4x + 7"
print(solution("x + x + x")) # "3x"
