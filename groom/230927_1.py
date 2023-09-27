# 구름LEVEL
# 문자열 나누기
# https://level.goorm.io/exam/195688/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%98%EB%88%84%EA%B8%B0/quiz/1

n = int(input())
s = input()

def split_into_three(s):
	n = len(s)
	result = []
	com_list = []
	for i in range(1, n-1):  # 첫 번째 분리점
		for j in range(i+1, n):  # 두 번째 분리점
			part1 = s[:i]
			result.append(part1)
			part2 = s[i:j]
			result.append(part2)
			part3 = s[j:]
			result.append(part3)
			com_list.append((part1, part2, part3))
	return result, com_list
	
split_list, score_list = split_into_three(s)
split_set = sorted(list(set(split_list)))
score_list = [sum([split_set.index(j)+1 for j in i]) for i in score_list]
print(max(score_list))
		
# 4
# abcd

# 14

# 3
# abz

# 6