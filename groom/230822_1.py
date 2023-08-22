# 구름LEVEL
# 카드 모으기
# https://level.goorm.io/exam/175909/%EC%B9%B4%EB%93%9C-%EB%AA%A8%EC%9C%BC%EA%B8%B0/quiz/1

n,m = map(int, input().split())
c = set()
result = -1
for i in range(m):
	k = int(input())
	c.add(k)
	if result == -1 and len(c) >= n:
		result = i+1
print(result)

# 예시1
# 입력
# 4 10
# 2
# 1
# 1
# 1
# 1
# 4
# 3
# 1
# 4
# 2
# 출력
# 7


# 예시2
# 입력
# 6 10
# 4
# 5
# 6
# 5
# 2
# 1
# 4
# 5
# 6
# 1
# 출력
# -1