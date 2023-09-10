# 구름LEVEL
# 규칙 숫자 야구
# https://level.goorm.io/exam/175928/%EA%B7%9C%EC%B9%99-%EC%88%AB%EC%9E%90-%EC%95%BC%EA%B5%AC/quiz/1

answer = list(map(int, input().rstrip()))
start = list(map(int, input().rstrip()))

def check(a, s):
    temp = []
    for a_i, s_i in zip(a, s):
        if s_i in a:
            if a_i == s_i:
                temp.append("s")
            else:
                temp.append("b")
        else:
            temp.append("f")
    return temp

result = 0
while True:
    game = check(answer, start)
    set_game = set(game)
    
    # 정답과 일치하는 경우
    if len(set_game) == 1 and set_game.pop() == "s":
        result += 1
        break

    # Fail인 경우를 먼저 처리
    for i, g in enumerate(game):
        if g == "f":
            t = (start[i]+1) % 10
            while t in start:
                t = (t+1) % 10
            start[i] = t

    # 다시 check하여 Ball 처리
    game = check(answer, start)
    ball_adjusted = False
    for i, g in enumerate(game):
        if g == "b" and not ball_adjusted:
            non_strike_indices = [i for i, g in enumerate(game) if g != "s"]
            start_values = [start[i] for i in non_strike_indices]
            start_values = start_values[-1:] + start_values[:-1]
            for i, value in zip(non_strike_indices, start_values):
                start[i] = value
            ball_adjusted = True
    
    result += 1

print(result)


# 1234
# 0123

# 4

# 1234
# 1234

# 1