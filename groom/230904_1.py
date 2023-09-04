# 구름LEVEL
# 구름 아이돌
# https://level.goorm.io/exam/170831/%EA%B5%AC%EB%A6%84-%EC%95%84%EC%9D%B4%EB%8F%8C/quiz/1

n = int(input())
n_list = list(map(int, input().split()))
i_n_list = [[i+1, v] for i, v in enumerate(n_list)]
idols = sorted(i_n_list, key=lambda x:-x[1])[:3]
print(" ".join(map(str, [i[0] for i in idols])))


# 5
# 10 3 7 4 1

# 1 3 4
 
# 7
# 7 2 6 4 9 8 1

# 5 6 1
