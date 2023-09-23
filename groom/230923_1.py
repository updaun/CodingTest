# 구름LEVEL
# 프로젝트 매니징
# https://level.goorm.io/exam/195684/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%A7%A4%EB%8B%88%EC%A7%95/quiz/1

from datetime import datetime, timedelta
n = int(input())
t, m = map(int, input().split())
now = datetime.now().replace(hour=t, minute=m)
for i in range(n):
	p = int(input())
	now += timedelta(minutes=p)
print(now.hour, now.minute)

# 3
# 10 10
# 50
# 22
# 23

# 11 45

# 4
# 23 40
# 1000
# 1000
# 880
# 20

# 0 0