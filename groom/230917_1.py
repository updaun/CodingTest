# 구름LEVEL
# 계수기 만들기
# https://level.goorm.io/exam/43061/%EA%B3%84%EC%88%98%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

m = int(input())
n = list(map(int, input().split()))
a = list(map(int, input().split()))
k = int(input())

def check(n, a):
	for i in range(m-1, -1, -1):
		if n[i] < a[i]:
			if i == 0:
				return -1
			a[i-1] += 1
			a[i] = 0
			return check(n, a)  # 자리올림이 발생했으면 함수를 다시 호출
	return a

for i in range(k):
	
	a[m-1] += 1
	a = check(n, a)
	if a == -1:
		print(-1)
		break
else:
	print("".join(map(str, a)))