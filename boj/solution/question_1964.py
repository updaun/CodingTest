# n = int(input())
# p_list = [1]
# for i in range(n):
#     p_list.append(3*i+4)
# print(sum(p_list)%45678)

# 더 빠른 풀이(등차수열)
n = int(input())
print((n*(3*n+5)//2+1)%45678)