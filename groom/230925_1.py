# 구름LEVEL
# 완벽한 햄버거 만들기
# https://level.goorm.io/exam/195686/%EC%99%84%EB%B2%BD%ED%95%9C-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

n = int(input())
n_list = list(map(int, input().split()))
max_n = max(n_list)
max_index = n - n_list[::-1].index(max_n) - 1
if n_list[:max_index+1] != sorted(n_list[:max_index+1]) or n_list[max_index+1:] != sorted(n_list[max_index+1:], reverse=True):
	print(0)
else:
	print(sum(n_list))
		
# 5
# 1 2 3 3 1

# 10

# 7
# 1 2 3 5 2 3 1

# 0