s_list = [i for i in input().upper()]
kv_list = [(i, s_list.count(i)) for i in set(s_list)]
kv_list = sorted(kv_list, key=lambda x:x[1], reverse=True)
if len(kv_list) == 1: print(kv_list[0][0])
elif kv_list[0][1] == kv_list[1][1]: print("?")
else: print(kv_list[0][0])