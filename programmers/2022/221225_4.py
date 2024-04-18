# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 다음 큰 숫자


def solution(n):
    bin_n = bin(n)[2:]
    temp = n+1
    bin_temp = bin(temp)[2:]
    if "0" not in bin_n:
        bin_n = "10" + bin_n[1:]
        return int(bin_n, 2)
    else:
        while bin_n.count("1") != bin_temp.count("1"):
            bin_temp = bin(temp)[2:]
            temp += 1
        return int(bin_temp, 2)

print(solution(78)) # 83
print(solution(15)) # 23