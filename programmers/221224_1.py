# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 이진 변환 반복하기

def solution(s):
    zero_count = 0
    count = 0
    while s != "1":
        while "0" in s:
            zero_count += s.count("0")
            s = s.replace("0", "")
        s = bin(len(s))[2:]
        count += 1
    return [count, zero_count]

print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]