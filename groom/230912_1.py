# 구름LEVEL
# 딱지놀이
# https://level.goorm.io/exam/48130/%EB%94%B1%EC%A7%80%EB%86%80%EC%9D%B4/quiz/1

n = int(input())
player = ["A", "B"]
card_types = ["4", "3", "2", "1"]
for i in range(n):
	dict_a, dict_b = dict(), dict()
	for c in card_types:
		dict_a[c] = 0
		dict_b[c] = 0
	a = input().split()
	b = input().split()
	for a_i in a[1:]:
		if a_i in dict_a.keys():
			dict_a[a_i] += 1
	for b_i in b[1:]:
		if b_i in dict_b.keys():
			dict_b[b_i] += 1

	for k in card_types:
		card = [dict_a[k], dict_b[k]]
		if dict_a[k] != dict_b[k]:
			print(player[card.index(max(dict_a[k],dict_b[k]))])
			break
	else:
		print("D")
print()

# 5
# 1 4
# 4 3 3 2 1
# 5 2 4 3 2 1
# 4 4 3 3 1
# 4 3 2 1 1
# 4 2 3 2 1
# 4 4 3 2 1
# 3 4 3 2
# 5 4 4 2 3 1
# 5 4 2 4 1 3

# A
# B
# B
# A
# D


# 4
# 4 4 3 2 1
# 4 1 4 3 2
# 4 3 3 2 1
# 4 4 3 3 3
# 4 4 3 3 3
# 4 3 4 3 2
# 4 3 2 1 1
# 3 3 2 1

# D
# B
# A
# A
