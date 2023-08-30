# 구름LEVEL
# 8진수 계산기
# https://level.goorm.io/exam/173337/8%EC%A7%84%EC%88%98-%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

# 8진수 변환
n = int(input())
n_list = list(map(int, input().split()))
print(oct(sum(n_list))[2:])

# 4
# 1 2 3 4

# 12

# 3
# 8 8 8

# 30
