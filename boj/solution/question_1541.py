import sys
input_text = sys.stdin.readline().strip()
input_list = []
temp = ''
for i in input_text:
    if i.isdigit():
        temp += i
    else:
        input_list.append(temp)
        temp = ''
        input_list.append(i)
if temp != '':
    input_list.append(temp)
answer = int(input_list[0])
flag = False
for i in range(1, len(input_list)):
    if input_list[i] == '-':
        flag = True
    if flag and input_list[i].isdigit():
        answer -= int(input_list[i])
    elif not flag and input_list[i].isdigit():
        answer += int(input_list[i])
print(answer)
