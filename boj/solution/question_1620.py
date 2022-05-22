import sys
N,M =list(map(int, sys.stdin.readline().split()))
pokemon_dict = dict()
number = 1
for i in range(N):
    pokemon_dict[sys.stdin.readline().strip()] = number
    number += 1
pokemon_list = list(pokemon_dict.keys())
question_list = []
for i in range(M):
    question_list.append(sys.stdin.readline().strip())
for question in question_list:
    if question.isalpha():
        print(pokemon_dict[question])
    else:
        print(pokemon_list[int(question)-1])  