# 구름LEVEL
# 이진수 정렬
# https://level.goorm.io/exam/195687/%EC%9D%B4%EC%A7%84%EC%88%98-%EC%A0%95%EB%A0%AC/quiz/1

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
s_list = sorted(n_list, key=lambda x:(-bin(x).count("1"), -x))
print(s_list[k-1])
		
# 8 6
# 1 2 3 4 5 6 7 8

# 4

# 7 1
# 1 2 4 8 16 32 64

# 64