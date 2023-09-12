# 구름LEVEL
# 소금물의 농도 구하기
# https://level.goorm.io/exam/194193/%EC%86%8C%EA%B8%88%EB%AC%BC%EC%9D%98-%EB%86%8D%EB%8F%84-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

import math
n, m = map(int, input().split())
salt = n*0.07
print(f"{math.floor(salt/(n+m)*10000)/100:.2f}")

# 1000 1000

# 3.50

# 100 150

# 2.80