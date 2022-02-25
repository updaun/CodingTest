s = input()
i_list = [-1 for i in range(26)]
a = 'abcdefghijklmnopqrstuvwxyz'
result = ''
for index, alphabet in enumerate(s):
    if i_list[a.find(alphabet)] == -1:
        i_list[a.find(alphabet)] = index
for i, n in enumerate(i_list):
    result += str(n)
    result += ' '
print(result)