# 구름LEVEL
# M배 배열
# https://level.goorm.io/exam/174909/m%EB%B0%B0-%EB%B0%B0%EC%97%B4/quiz/1

n, k = map(int, input().split())
m_list = list(map(int, input().split()))
print(" ".join(map(str, [i if i%k==0 else i*k for i in m_list])))

# 예시1
# 입력
# 7 3
# 1 2 3 4 5 6 7
# 출력
# 3 6 3 12 15 6 21


# 예시2
# 입력
# 5 5
# 5 10 15 20 25
# 출력
# 5 10 15 20 25