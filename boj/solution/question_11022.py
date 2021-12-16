n = int(input())
answer_list = []
for i in range(n):
    a, b = map(int, input().split())
    answer_list.append([a,b,a+b])

for i in range(len(answer_list)):
    print(f'Case #{i+1}: {answer_list[i][0]} + {answer_list[i][1]} = {answer_list[i][2]}')
    