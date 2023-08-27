# 구름LEVEL
# 연속 점수
# https://level.goorm.io/exam/174924/%EC%97%B0%EC%86%8D-%EC%A0%90%EC%88%98/quiz/1

# 나의 풀이(n^2)
n = int(input())
n_list = list(map(int, input().split()))
result = []
for i in range(n):
	temp = n_list[i]
	start = temp
	for j in range(i+1, n):
		next_number = n_list[j]
		if next_number-start == 1:
			temp += next_number
			start = next_number
		else:
			break
	result.append(temp)
print(max(result))

# 다른 사람의 풀이(n)
n = int(input())
n_list = list(map(int, input().split()))

max_sum = 0
current_sum = n_list[0]
for i in range(1, n):
    # 연속된 숫자인 경우 합을 누적
    if n_list[i] == n_list[i - 1] + 1:
        current_sum += n_list[i]
    # 연속되지 않는 경우, 현재까지의 합과 최대 합을 비교하고 초기화
    else:
        max_sum = max(max_sum, current_sum)
        current_sum = n_list[i]
max_sum = max(max_sum, current_sum)

print(max_sum)

# 5
# 2 3 4 5 6

# 20

# 7
# 1 2 1 2 1 2 4

# 4