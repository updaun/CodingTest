subject_cnt = int(input())
subject_list = list(map(int, input().split()))

print(round((sum(subject_list)/subject_cnt) / max(subject_list) * 100, 6))