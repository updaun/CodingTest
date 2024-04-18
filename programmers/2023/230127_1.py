# 프로그래머스
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 다트 게임

def solution(dartResult):
    stack = []
    score = {"S":1, "D":2, "T":3}
    temp = ""
    temp1 = None
    temp2 = None
    dart_list = []
    for i in dartResult:
        temp += i
        if not i.isdigit():
            dart_list.append(temp)
            temp = ""
    for case in dart_list:
        s = case[-1]
        if s.isalpha():
            stack.append(int(case[:-1])**score[s])
        elif s == "*":
            if stack:
                temp1 = stack.pop()*2
            if stack:
                temp2 = stack.pop()*2
            if temp2:
                stack.append(temp2)
                temp2 = None
            if temp1:
                stack.append(temp1)
                temp1 = None
        elif s == "#":
            if stack:
                stack.append(stack.pop()*-1)
    return sum(stack)

print(solution("1S2D*3T")) # 37
print(solution("1D2S#10S")) # 9
print(solution("1D2S0T")) # 3
print(solution("1S*2T*3S")) # 23
print(solution("1D#2S*3S")) # 5
print(solution("1T2D3D#")) # -4
print(solution("1D2S3T*")) # 59
print(solution("1S2D*3T*")) # 72
print(solution("1S2D3T*")) # 63