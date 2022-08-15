import sys
input = sys.stdin.readline
for i in range(int(input())):
    n,m = map(int, input().split())
    result = (m-n+1) * (n+m)//2
    print(f"Scenario #{i+1}:")
    print(f"{result}\n")
   
# 내가 생각한 방법으로는 왜 수식 구현을 할 수 없는가?
# 정답 : 440625159107385260
# 계산값 : 440625159107385280
# n, m = -89173, 938749341  
# n, m = -11, 10
# n, m = 1, 100

# print(int((m-n+1)/2 * (m+n)))
# print(int((m-n)/2 * (m-1+n))+ m)