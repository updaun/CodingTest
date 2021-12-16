n = input()
count = 1

if len(n)==1:
    n = "0" + n

n_str = n

while True:
    n_str = n_str[-1] + (str(int(n_str[0])+int(n_str[1])))[-1]
    if (n == n_str):
        break
    count += 1
print(count)