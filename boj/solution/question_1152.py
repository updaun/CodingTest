word_list = input().strip().split(" ")
result = [i.strip() for i in word_list if i != ""]
print(len(result))