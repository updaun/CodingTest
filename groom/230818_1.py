# 구름LEVEL
# 의좋은 형제
# https://level.goorm.io/exam/49088/%EC%9D%98%EC%A2%8B%EC%9D%80-%ED%98%95%EC%A0%9C/quiz/1


j, s = list(map(int, input().split()))
day = int(input())
for i in range(1, day+1):
	if i % 2 != 0:
		temp = j//2
		j, s = temp,s+(j-temp)
	else:
		temp = s//2
		j, s = j+(s-temp), temp
print(j, s)

# 예시1
# 입력
# 100 100
# 4
# 출력
# 131 69


# 예시2
# 입력
# 70 100
# 1
# 출력
# 35 135


# 예시3
# 입력
# 1 1
# 9
# 출력
# 0 2


# 예시4
# 입력
# 537 141
# 11
# 출력
# 226 452
