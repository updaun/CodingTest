s = input()
cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in cro_list:
    if i in s:
        s = s.replace(i, "$")
print(len(s))